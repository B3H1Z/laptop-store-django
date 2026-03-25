import sqlite3

from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import permission_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render

from store.forms import SignUpForm


def selectAllProducts():
	connection = sqlite3.connect("db.sqlite3")
	cursor = connection.cursor()
	x = cursor.execute("Select * from Products")
	prodocts = x.fetchall()
	context = {
		"laptops": []
	}
	for prodoct in prodocts:
		context['laptops'].append({
			"id": prodoct[0],
			"brand": prodoct[1],
			"model": prodoct[2],
			"size": prodoct[3],
			"cpuGen": prodoct[4],
			"cpuModel": prodoct[5],
			"ramSize": prodoct[6],
			"ramSizeUnit": prodoct[7],
			"diskSize": prodoct[8],
			"diskSizeUnit": prodoct[9],
			"diskType": prodoct[10],
			"graphicModel": prodoct[11],
			"graphicSeries": prodoct[12],
			"usageType": prodoct[13],
			"price": f"{prodoct[14]:,}",
			"description": prodoct[15],
			"image": prodoct[16],
			"hoverImage": prodoct[17]
		})
	return context


def home(request):
	context = selectAllProducts()
	return render(request, 'index.html', context)


@permission_required('auth.view_user')
def newProduct(request):
	return render(request, 'add_new_laptop.html')


def addNewProduct(request):
	if request.method != 'POST':
		return redirect('/accounts/admin/dashboard')

	main_image = request.FILES['image']
	hover_image = request.FILES['hoverImage']
	fss = FileSystemStorage()
	file = fss.save(main_image.name, main_image)
	hover_file = fss.save(hover_image.name, hover_image)
	file_url = fss.url(file)
	hover_file_url = fss.url(hover_file)

	connection = sqlite3.connect("db.sqlite3")
	cursor = connection.cursor()

	cursor.execute("INSERT INTO Products VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
				   (request.POST['id'],
					request.POST['brand'],
					request.POST['model'],
					request.POST['size'],
					request.POST['cpuGen'],
					request.POST['cpuModel'],
					request.POST['ramSize'],
					request.POST['ramSizeUnit'],
					request.POST['diskSize'],
					request.POST['diskSizeUnit'],
					request.POST['diskType'],
					request.POST['graphicModel'],
					request.POST['graphicSeries'],
					request.POST['usageType'],
					request.POST['price'],
					request.POST['description'].encode('utf-8'),
					file_url,
					hover_file_url))
	connection.commit()
	connection.close()

	return redirect('/accounts/admin/dashboard')


def userDashboard(request):
	return render(request, 'my_account.html')


def adminDashboard(request):
	context = selectAllProducts()
	connection = sqlite3.connect("db.sqlite3")
	cursor = connection.cursor()
	cursor.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM Products")
	context['next_product_id'] = cursor.fetchone()[0]
	connection.close()
	return render(request, 'admin_panel.html', context)


def signup_view(request):
	form = SignUpForm(request.POST)
	if form.is_valid():
		user = form.save()
		user.refresh_from_db()
		user.profile.first_name = form.cleaned_data.get('first_name')
		user.profile.last_name = form.cleaned_data.get('last_name')
		user.profile.email = form.cleaned_data.get('email')
		user.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		return redirect('/accounts/login')
	else:
		form = SignUpForm()
	return render(request, 'registration/signup.html', {'form': form})


def products(request):
	context = selectAllProducts()
	return render(request, 'shop_3_column.html', context)


def page_not_found_view(request, exception):
	return render(request, '404.html', status=404)


def about(request):
	return render(request, 'about.html')


def user(request):
	if request.user.is_authenticated:
		if request.user.has_perm('auth.view_user'):
			return redirect('/accounts/admin/dashboard')
		else:
			return redirect('/accounts/dashboard')
	return redirect('/accounts/login')


def product(request, id):
	connection = sqlite3.connect("db.sqlite3")
	cursor = connection.cursor()
	cursor.execute("Select * from Products where id = ?", (id,))
	prodoct = cursor.fetchone()
	context = {
		"laptop": {
			"id": prodoct[0],
			"brand": prodoct[1],
			"model": prodoct[2],
			"size": prodoct[3],
			"cpuGen": prodoct[4],
			"cpuModel": prodoct[5],
			"ramSize": prodoct[6],
			"ramSizeUnit": prodoct[7],
			"diskSize": prodoct[8],
			"diskSizeUnit": prodoct[9],
			"diskType": prodoct[10],
			"graphicModel": prodoct[11],
			"graphicSeries": prodoct[12],
			"usageType": prodoct[13],
			"price": f"{prodoct[14]:,}",
			"shortDescription": prodoct[15].decode('utf8')[:100] + "...",
			"description": prodoct[15].decode('utf8'),
			"image": prodoct[16],
			"hoverImage": prodoct[17],
		}
	}

	return render(request, 'single_product.html', context)


def logout_view(request):
	logout(request)
	return redirect('/')
