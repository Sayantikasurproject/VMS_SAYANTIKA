# VMS_SAYANTIKA
visitor_management_system
1.	manage.py: A command-line utility to interact with the Django project. You use it to run management commands, like creating database tables and managing migrations.
2.	__init__.py: An empty file that tells Python that this directory should be considered a Python package.
3.	settings.py: Contains settings for your Django project, including database configuration, time zone, static files, etc.
4.	urls.py: Defines the URL patterns for your Django project, mapping URLs to views.
5.	asgi.py: Configures the ASGI (Asynchronous Server Gateway Interface) entry point for your project.

visitor_app
1.	migrations/: Directory to store database migration files. Migrations are used to apply changes to the database schema over time.
2.	static/css/: Folder for storing static CSS files.
3.	templates/: Directory for storing HTML templates.
•	alldata.html: Represents a page displaying all data.
•	barcode.html: Represents a page related to barcode functionality.
•	category.html: Represents a page related to visitor categories.
•	Department.html: Represents a page related to staff departments.
•	enterprise.html: Represents a page for managing organization details.
•	login.html: Represents the login page.
•	postal.html: Represents a page for managing postal service details.
•	Reports.html: Represents a page for viewing reports.
•	staffmaster.html: Represents a page for managing staff details.
•	usermaster.html: Represents a page for managing user accounts.
•	visitorregistration.html: Represents a page for visitor registration.
•	visitorlogout.html: Represents a page for visitor logout.
4.	__init__.py: An empty file to make the directory a Python package.
5.	admin.py: Configuration for Django Admin. You can register models here to manage them through the Django Admin interface.
6.	apps.py: Configuration for the app.
7.	models.py: Defines the data models for the app.
8.	static_root/: A folder that can be used to collect static files during deployment.
9.	tests.py: File for writing tests for your app.
10.	urls.py: Defines the URL patterns specific to the app.
11.	views.py: Contains the views (functions or classes) that handle HTTP requests for your app.
static/:
1.	images/: A folder for storing static image files.
media_root/:
1.	A folder that can be used to store user-uploaded media files.
db.sqlite3:
1.	The SQLite database file where your application data is stored.



Functionalities:
•	Masters Module:
•	Enterprise Master: Manage organization details.
•	Category Master: Manage visitor categories.
•	Department Master: Manage staff departments.
•	Staff Master: Manage staff details.
•	User Master: Manage user accounts (Admin, User, Security).
•	Postal Service Module: Manage incoming and outgoing postal service details.
•	VMS (Visitor Management System):
•	Login Page: Staff members log in using their credentials.
•	Visitor Registration: Register new visitors and update existing visitor details.
•	Visitor Logout: Log out visitors.
•	Multiple Day Login/Logout: For passes valid for multiple days.
•	Visitor Reports Module:
•	Visitor Details: View details of visitors in and out.
•	Reports: Generate and view various reports related to visitors, postal services, user logins, and multiple-day passes

visitor_management_system/( FILESTRUCTURE)
├── manage.py
├── visitor_management_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
├── visitor_app/
│   ├── migrations/
│   │   └── __init__.py
│   ├── static/
│   │   └── css/
│   │       └── styles.css
│   ├── templates/
│   │   └── vms_templates/
│   │       ├── alldata.html
│   │       ├── barcode.html
│   │       ├── category.html
│   │       ├── Department.html
│   │       ├── enterprise.html
│   │       ├── login.html
│   │       ├── postal.html
│   │       ├── Reports.html
│   │       ├── staffmaster.html
│   │       ├── usermaster.html
│   │       ├── visitorregistration.html
│   │       └── visitorlogout.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── static_root/
│   ├── templates/
│   │   └── visitor_app_templates/
│   │       └── base_generic.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/
│   └── images/
│       └── image.jpg
├── media_root/
└── db.sqlite3
