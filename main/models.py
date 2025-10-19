from subprocess import check_output

from django.contrib.auth.models import AbstractUser
from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length=150)
    aktiv = models.BooleanField()
    def __str__(self):
        return self.nom

class Fan(models.Model):
    nom = models.CharField(max_length=150)
    asosiy = models.BooleanField()
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Ustoz(models.Model):
    ism = models.CharField(max_length=150)
    yosh = models.PositiveIntegerField()
    gender = models.CharField(max_length=150, choices=[('erkak', 'Erkak'), ('ayol', 'Ayol')])
    daraja = models.CharField(max_length=150, choices=[('bakalavr', 'Bakalavr'), ('magistr', 'Magister')])
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism
