from django.db import models


class Tour(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    short_annotation = models.CharField(max_length=100)
    date_add = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=32)
    image = models.ImageField(upload_to='img/')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    view_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
