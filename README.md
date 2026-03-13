
# Django Cars Project

## Overview

This project demonstrates the basic setup of a Django web application. Django is a high-level Python web framework that follows the Model-View-Template (MVT) architecture and helps developers build web applications quickly and efficiently.

The project includes:

* Django project setup
* Application creation
* Basic view returning an HTTP response
* Static and template folders
* Model creation and migration
* Admin panel configuration

---

# Technologies Used

* Python
* Django
* HTML
* CSS
* JavaScript

---

# Project Setup

## 1. Create Virtual Environment

```
python -m venv venv
```

## 2. Activate Virtual Environment

### Windows

```
venv\Scripts\activate
```

### macOS / Linux

```
source venv/bin/activate
```

---

# Install Dependencies

Upgrade pip:

```
python -m pip install --upgrade pip
```

Install Django:

```
pip install Django
```

Check Django version:

```
django-admin --version
```

---

# Create Django Project

```
django-admin startproject cars_project
```

---

# Run Development Server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

Stop server:

```
Ctrl + C
```

---

# Create Django App

```
python manage.py startapp cars_app
```

Add the app in `settings.py`.

---

# Create Basic View

Example in `views.py`:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```

---

# Database Setup

Run initial migration:

```
python manage.py migrate
```

After creating models:

```
python manage.py makemigrations
python manage.py migrate
```

---

# Create Superuser

```
python manage.py createsuperuser
```

Login to admin panel:

```
http://localhost:8000/admin
```

---

# Project Structure

```
cars_project/
│
├── cars_project/
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
│
├── cars_app/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
│
├── templates/
│   ├── pages/
│   └── extra/
│
├── static/
│   ├── assets/
│   ├── css/
│   └── js/
│
├── manage.py
└── db.sqlite3
```

---

# Static Files

Use Django static tags:

```
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

---

# Features

* Django MVT architecture
* Admin dashboard
* Static and template management
* Database migrations
* Basic view routing

---

# Author
**Shajitha Begam**  
GitHub: https://github.com/ShajiHub
Django learning project created for Education and Training Django framework setup.
