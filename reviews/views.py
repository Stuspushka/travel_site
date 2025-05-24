from django.shortcuts import render, redirect

from .models import Review
from .forms import ReviewForm


def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, user=request.user)
        if form.is_valid():
            review = form.save(commit=False)
            if request.user.is_authenticated:
                review.name = request.user.get_full_name() or request.user.username
            else:
                review.name = "Аноним"
            review.save()
            return redirect('reviews')
    else:
        form = ReviewForm(user=request.user)
    reviews = Review.objects.all().order_by('-date_add')
    return render(request, 'reviews.html', {'form': form, 'reviews': reviews})
