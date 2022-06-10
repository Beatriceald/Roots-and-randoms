from django.db import models
from django.urls import reverse

class EquationValues(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()

    def get_absolute_url(self):
        return reverse('solution', kwargs={'pk': self.pk})