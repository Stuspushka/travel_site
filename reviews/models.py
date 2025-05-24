from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} – {self.rating}/5"
