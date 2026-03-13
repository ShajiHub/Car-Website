from django.urls import path
from cars_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path('inventory/', views.inventory, name='inventory'),
    path('about/', views.about, name='about'),
]
