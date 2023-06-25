from django.urls import path
from . import views
from .models import Employer  # Не забудьте про этот импорт

# Остальной код...


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('output/', views.output, name='output'),

]