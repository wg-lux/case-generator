from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='endoscopy_anticoagulation_home'),
]
