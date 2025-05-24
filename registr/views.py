from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from cart.models import CartItem, Cart, Order
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Sum


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registr.html', {'form': form})


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        if not request.POST.get('remember_me'):
            request.session.set_expiry(0)
        else:
            request.session.set_expiry(60 * 60 * 24 * 30)
        return redirect('index')
    return render(request, 'login.html', {'form': form})


def profile_view(request):
    if request.user.is_authenticated:
        active_cart = Cart.objects.filter(user=request.user, is_active=True)
        cart_count = CartItem.objects.filter(cart__in=active_cart).aggregate(
            total=Sum('quantity')
        )['total'] or 0
        current_orders = Order.objects.filter(user=request.user, status='in_process')
        past_orders = Order.objects.filter(user=request.user, status='completed')
        return render(request, 'profile.html', {
            'current_orders': current_orders,
            'past_orders': past_orders,
            'cart_count': cart_count,
        })
    return redirect('login')
