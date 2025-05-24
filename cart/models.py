# models.py
from django.db import models
from django.contrib.auth.models import User
from TourList.models import Tour

# Модель корзины
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

# Модель товара в корзине
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.tour.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.tour.title}"

# Модель заказа
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('in_process', 'В процессе'), ('completed', 'Завершён')])
    email = models.EmailField(default=None,unique=False)
    phone = models.CharField(max_length=20, default=None,unique=False)
    booking_date = models.DateField(default=None, unique=False)
    full_name = models.CharField(max_length=100, default=None,unique=False)

    def __str__(self):
        return f"Заказ пользователя {self.user.username} - Статус: {self.status}"

    @property
    def total_price(self):
        items = self.cart.items.all()
        return sum(item.tour.price * item.quantity for item in items)