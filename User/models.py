from django.contrib.auth.models import User
from django.db import models


class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveIntegerField()
    kasb = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Maqola(models.Model):
    sarlavha = models.CharField(max_length=50)
    sana = models.DateField()
    mavzu = models.TextField()
    matn = models.TextField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

