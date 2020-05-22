from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactSubmit, name='contactSubmit'),
]