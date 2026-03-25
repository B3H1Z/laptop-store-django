"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from store import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='home'),
                  path('manage/product', views.newProduct, name='newProduct'),
                  path('manage/product/submit', views.addNewProduct, name='addNewProduct'),
                  # path('login', views.login, name='login'),
                  # path('singup', views.singup, name='singup'),
                  # path('login/submit', views.loginSubmit, name='loginSubmit'),
                  path('accounts/dashboard', views.userDashboard, name='userDashboard'),
                  path('accounts/admin/dashboard', views.adminDashboard, name='adminDashboard'),
                  path('user/logout', views.logout_view, name='logout_view'),
                  path('accounts/', include("django.contrib.auth.urls"),
                       ),

                  path('accounts/signup', views.signup_view, name="signup"),
                  path('products', views.products, name='products'),
                  path('about', views.about, name='about'),
                  path('product/<int:id>', views.product, name='product'),
                  path('user', views.user, name='user'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
