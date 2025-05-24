from django.urls import path
from TourList import views

urlpatterns = [
    path('tours/', views.tour_list, name='tours'),
    path('tour/<tour_id>', views.one_tour, name='onetour'),
]