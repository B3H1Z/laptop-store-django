# Laptop Store Django

A modern e-commerce web application for buying and selling laptops, built with Django.

## Features

- **Product Catalog**: Browse and view detailed information about laptops
- **Admin Panel**: Manage products, orders, and users
- **User Authentication**: Secure login and account management
- **Responsive Design**: Mobile-friendly interface with Bootstrap
- **Image Gallery**: Product zoom and gallery functionality
- **Shopping Experience**: Add to cart and manage orders

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- virtualenv or venv

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/laptop-store-django.git
   cd laptop-store-django
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser account**
   ```bash
   python manage.py createsuperuser
   ```

## Usage

1. **Start the development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

3. **Login to admin**
   - Use the superuser credentials created during installation

## Project Structure

```
laptop-store-django/
├── djangoProject/          # Main Django project settings
│   ├── settings.py         # Project configuration and environment variables
│   ├── urls.py             # URL routing
│   ├── views.py            # Shared views
│   ├── forms.py            # Shared forms
│   └── wsgi.py             # WSGI configuration for deployment
├── store/                  # Main application
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── admin.py            # Admin interface configuration
│   ├── tests.py            # Test suite
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   └── static/             # CSS, JavaScript, images, fonts
├── manage.py               # Django management utility
├── requirements.txt        # Python dependencies
├── .env.example            # Template for environment variables
└── README.md               # This file
```

## Database

The application uses SQLite for development, which is included by default. For production deployments:

1. Set the `DATABASE_URL` environment variable:
   ```bash
   DATABASE_URL=postgresql://user:password@localhost/dbname
   ```

2. Install the appropriate database driver:
   ```bash
   pip install psycopg2-binary  # For PostgreSQL
   ```

## Environment Variables

The application uses environment variables for configuration. Create a `.env` file in the project root (use `.env.example` as a template):

- **SECRET_KEY**: Django secret key for session encryption (defaults to dev key)
- **DEBUG**: Set to `True` for development, `False` for production (defaults to `False`)
- **ALLOWED_HOSTS**: Comma-separated list of allowed hostnames (defaults to `localhost,127.0.0.1`)
- **DATABASE_URL**: Database connection string (defaults to SQLite)

Example `.env` file:
```
SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

## Running Tests

Execute the test suite:
```bash
python manage.py test
```

Run tests for a specific app:
```bash
python manage.py test store
```

Run a specific test class:
```bash
python manage.py test store.tests.StoreViewTests
```

## Static Files

Collect static files for production:
```bash
python manage.py collectstatic
```

Static files are served from `/static/` and include:
- CSS files (Bootstrap, Font Awesome, custom styles)
- JavaScript (jQuery, plugins, custom scripts)
- Fonts (Raleway, Far Yekan, Ramola)
- Images (products, banners, icons)

## Admin Interface

Access the Django admin at `/admin` with your superuser account to:
- Manage laptop products
- View and update orders
- Manage user accounts
- Configure site settings

## Deployment

For production deployment:

1. Set `DEBUG=False` in your environment
2. Set a strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS` with your domain
4. Use a production database (PostgreSQL recommended)
5. Use a production WSGI server (Gunicorn recommended)
6. Set up static file serving (WhiteNoise or CDN)
7. Enable HTTPS

See `djangoProject/wsgi.py` for WSGI configuration.

## Troubleshooting

**Import errors or packages not found**
- Ensure your virtual environment is activated
- Run `pip install -r requirements.txt`

**Database errors**
- Run `python manage.py migrate` to create tables
- Check DATABASE_URL configuration

**Static files not loading**
- Run `python manage.py collectstatic`
- Check STATIC_URL and STATIC_ROOT in settings.py

**Admin panel issues**
- Create a new superuser: `python manage.py createsuperuser`
- Clear browser cache

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an issue on GitHub or contact the development team.

---

**Last Updated**: March 2026
**Version**: 1.0.0
**Django Version**: 3.2.19
