from django.urls import path
from reviews import views

urlpatterns = [
    path('reviews/', views.reviews, name='reviews'),
]