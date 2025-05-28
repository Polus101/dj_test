from django.db import models

# Create your models here.
class Calc(models.Model):
    a = models.IntegerField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.a)