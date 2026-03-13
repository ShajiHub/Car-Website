from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
from django.http import HttpResponse

#include forms and models
from .forms import ContactForm, CarForm
from .models import Car


def home(request):
    featured_cars = [
        {
            'name': 'Toyota Corolla', 
            'year': 2025, 
            'transmission': 'Automatic', 
            'fuel': 'Petrol',
            'price': '$15,000',
            'image': 'https://picsum.photos/1400/800'
        },
        {'name': 'Honda CR-V', 
         'year': 2026, 
         'transmission': 'Automatic', 
         'fuel': 'Hybrid', 
         'price': '$22,500', 
         'image': 'https://picsum.photos/1400/800'
         },
        {'name': 'Hyundai i20', 'year': 2024,
         'transmission': 'Manual', 'fuel': 'Petrol', 'price': '$11,200', 'image': 'https://picsum.photos/1400/800'},
        {'name': 'Toyota Corolla', 'year': 2025, 'transmission': 'Automatic', 'fuel': 'Petrol', 'price': '$15,000', 'image': 'https://picsum.photos/1400/800'},
        {'name': 'Honda CR-V', 'year': 2026, 'transmission': 'Automatic', 'fuel': 'Hybrid', 'price': '$22,500', 'image': 'https://picsum.photos/1400/800'},
        {'name': 'Hyundai i20', 'year': 2024, 'transmission': 'Manual', 'fuel': 'Petrol', 'price': '$11,200', 'image': 'https://picsum.photos/1400/800'},
    ]

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            
            data = contact_form.cleaned_data

            name = data.get('name') or ""
            email = data.get('email') or ""
            message = data.get('message') or ""

            errors = {}

            if len(name) < 3:
                errors['name'] = "Name must be at least 3 characters long."

            if "spam" in message.lower():
                errors['message'] = "The word spam cannot be in message"

            # Email format validation
            try:
                validate_email(email)
            except ValidationError:
                errors['email'] = "Enter a valid email address."

            if errors:
                for field, error in errors.items():
                    contact_form.add_error(field, error)
            else:
                print(contact_form.cleaned_data)  # testing
                return redirect('home')

            #Here you can save form data or send an email
            # print(contact_form.cleaned_data)# for testing     
            # return redirect('home')
    else:
        contact_form = ContactForm()
    return render(request, 'pages/home.html', {'cars': featured_cars, 'contact_form': contact_form})

def inventory(request):
    if request.method == 'POST':
        inventory_form = CarForm(request.POST)
        if inventory_form.is_valid():
            inventory_form.save()
            return redirect('inventory')
    else:
        inventory_form = CarForm()
    # cars = Car.objects.all()
    return render(request, 'pages/inventory.html',{'inventory_form':inventory_form})

def about(request):
    return render(request, 'pages/about.html')


# def home(request):
#     return render(request, 'pages/home.html')