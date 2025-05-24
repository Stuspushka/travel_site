import re
from django.core.exceptions import ValidationError
from django import forms
from .models import Order
from datetime import date, timedelta

class BookingForm(forms.ModelForm):
    booking_date = forms.DateField(
        label="Дата поездки",
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=date.today
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = date.today()
        max_date = today + timedelta(days=180)
        self.fields['booking_date'].widget.attrs['min'] = today.strftime('%Y-%m-%d')
        self.fields['booking_date'].widget.attrs['max'] = max_date.strftime('%Y-%m-%d')

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone = re.sub(r'[\s\-\(\)]', '', phone)
        pattern = r'^(\+7|8|7)?\d{10}$'
        if not re.match(pattern, phone):
            raise ValidationError("Введите корректный номер: +7XXXXXXXXXX, 8XXXXXXXXXX или 79XXXXXXXXXX.")
        return phone

    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone', 'booking_date']
