from django.db import models

# Create your models here.

class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    ]

    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric'),
    ]

    name = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    fuel = models.CharField(max_length=20, choices=FUEL_CHOICES)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
# (actual_value, human_readable_name)
# Tuple of tuples (most common)