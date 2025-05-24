from django.shortcuts import render
from .models import Tour


def tour_list(request):
    tours = Tour.objects.all()
    sort_by = request.GET.get('sort')
    if sort_by == 'price':
        tours = tours.order_by('price')
    elif sort_by == 'price_desc':
        tours = tours.order_by('-price')
    elif sort_by == 'views_count':
        tours = tours.order_by('-view_count')
    else:
        tours = tours.order_by('-date_add')
    return render(request, 'tourlist.html', {'tours':tours})


def one_tour(request,tour_id):
    tour = Tour.objects.get(id=tour_id)
    tour.view_count += 1
    tour.save()
    return render(request,'onetour.html',{'tour':tour})
