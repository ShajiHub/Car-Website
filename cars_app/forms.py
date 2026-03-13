from django import forms
from .models import Car

class ContactForm(forms.Form):
    #creating fields we need
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Enter your message'
    }))

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        #adding only attributes to the fields
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Car Name'}),
            'year': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Year'}),
            'price': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Price'}),
            'transmission': forms.Select(attrs={'class': 'form-select'}),
            'fuel': forms.Select(attrs={'class': 'form-select'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
