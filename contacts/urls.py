from contacts import views
from django.urls import path

urlpatterns =[
    path('contacts/', views.contacts, name='contacts')
]