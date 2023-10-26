# myapp4/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact/create/', views.contact_create, name='contact_create'),
    path('contact/update/<int:pk>/', views.contact_update, name='contact_update'),
    path('contact/delete/<int:pk>/', views.contact_delete, name='contact_delete'),
]
