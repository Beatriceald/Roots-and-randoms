from django.db import models
from django.urls import reverse

# Create your models here.
class Ball(models.Model):
    ball = models.IntegerField()

    def get_absolute_url(self):
        return reverse('guess', kwargs={'pk': self.pk})
