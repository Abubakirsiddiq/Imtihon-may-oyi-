from django.shortcuts import render, redirect
from .models import *


class Login(models.Model):
    def get(self, request):
        return render(request, "login.html")


class Blog(models.Model):
    def get(self, request):
        return render(request, "blog.html")

    def post(self, request):
        a = Maqola.objects.create(
            sarlavha=request.POST.get("sarlavha"),
            sana=request.POST.get("sana"),
            mavzu=request.POST.get("mavzu"),
            matn=request.POST.get("matn"),
        )
        idsi=request.POST.get("muallif")
        mu=Muallif.objects.get(id=idsi)
        m = Maqola.objects.all()
        return redirect({"hammasi":m, "muallif":mu})


class Maqola(models.Model):
    def get(self, request):
        return render(request, "maqola.html")

    def post(self, request, pk):



