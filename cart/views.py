from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from TourList.models import Tour
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import BookingForm



@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user, is_active=True)

    if request.method == "POST":
        item_id = request.POST.get("item_id")
        action = request.POST.get("action")

        item = get_object_or_404(CartItem, id=item_id, cart=cart)

        if action == "increase":
            item.quantity += 1
            item.save()
        elif action == "decrease":
            if item.quantity > 1:
                item.quantity -= 1
                item.save()
        elif action == "remove":
            item.delete()

        return redirect("cart")

    return render(request, "cart.html", {"cart": cart})


@login_required
def add_to_cart(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    cart, _ = Cart.objects.get_or_create(user=request.user, is_active=True)
    item, created = CartItem.objects.get_or_create(cart=cart, tour=tour)

    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart')


def checkout_view(request):
    cart = Cart.objects.filter(user=request.user, is_active=True).first()
    if Order.objects.filter(cart=cart).exists():
        cart = Cart.objects.create(user=request.user, is_active=True)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            Order.objects.create(
                user=request.user,
                cart=cart,
                status='in_process',
                email=request.POST['email'],
                phone=request.POST['phone'],
                full_name=request.POST['full_name'],
                booking_date=request.POST['booking_date'],
                )
            cart.is_active = False
            cart.save()
            Cart.objects.create(user=request.user, is_active=True)
            return redirect('booking_confirmation')
    else:
        form = BookingForm()
    return render(request, 'checkout.html', {'form': form, 'cart': cart})


def booking_confirmation(request):
    return render(request, 'booking_confirmation.html')


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})
