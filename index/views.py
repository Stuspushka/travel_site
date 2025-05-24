from django.shortcuts import render
from TourList.models import Tour
from reviews.models import Review
from random import choices

def index(request):
    reviews = Review.objects.all()
    if reviews.count() < 6:
        reviews = reviews.order_by('-date_add')
    else:
        reviews = choices(reviews,k=6)
    tours = Tour.objects.order_by('view_count').reverse()[:6]
    return render(request, 'base.html',{'tours':tours, 'reviews':reviews})
