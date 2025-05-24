from django import forms
from .models import Review
from cart.models import Tour, Order, CartItem
from django.contrib.auth.models import AnonymousUser


class ReviewForm(forms.ModelForm):
    tour = forms.ModelChoiceField(
        queryset=Tour.objects.none(),
        label="Выберите тур",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and not isinstance(user, AnonymousUser):
            completed_orders = Order.objects.filter(user=user, status='completed')
            completed_tours = Tour.objects.filter(
                cartitem__cart__order__in=completed_orders
            ).distinct()
            self.fields['tour'].queryset = completed_tours
        else:
            self.fields['tour'].queryset = Tour.objects.none()

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) > 1000:
            raise forms.ValidationError("Отзыв не должен превышать 1000 символов.")
        return text

    class Meta:
        model = Review
        fields = ['text', 'tour', 'rating']
        widgets = {
            'rating': forms.Select(choices=[(i, f"{i} / 5") for i in range(1, 6)]),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4,
                                          'placeholder': 'Напишите ваш отзыв (не более 1000 символов)...'}),
        }
