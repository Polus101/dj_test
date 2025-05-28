from django.db import models

# Create your models here.

class Manager(models.Model):
    fio = models.TextField("ФИО")
    image = models.ImageField(upload_to="managers/", default="aboba")
    html_block = models.TextField("Код", default="")

    def __str__(self):
        return self.fio