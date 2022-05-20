from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FilmForm
from .models import Films
from . import models
from django import forms

def ajout(request):
    if request.method == "POST":
        form = FilmForm(request)
        if form.is_valid():
            films = form.save()
            return HttpResponseRedirect("/Horreur/")
        else:
            return render(request,"Horreur/ajout.html",{"form": form})
    else :
        form = FilmForm()
        return render(request,"Horreur/ajout.html",{"form" : form})

def traitement(request):
    fform = FilmForm(request.POST)
    if fform.is_valid():
        films = fform.save()
        return HttpResponseRedirect("/Horreur/")
    else:
        return render(request,"Horreur/ajout.html",{"form": fform})


def index(request):
    liste = list(models.Films.objects.all())
    return render(request, 'Horreur/index.html', {'liste': liste})

def affiche(request, id):
    films = models.Films.objects.get(pk=id)
    return render(request,"Horreur/affiche.html",{"Films" : films})

def delete(request, id):
    films = models.Films.objects.get(pk=id)
    films.delete()
    return HttpResponseRedirect("/Horreur/")

def update(request, id):
    Films = models.Films.objects.get(pk=id)
    fform = FilmForm(Films.dico())
    return render(request, "Horreur/update.html", {"form": fform,"id":id})

def traitementupdate(request, id):
    fform = FilmForm(request.POST)
    if fform.is_valid():
        films = fform.save(commit=False)
        films.id = id;
        films.save()
        return HttpResponseRedirect("/Horreur/")
    else:
        return render(request, "Horreur/update.html", {"form": fform, "id": id})

def ok(request):
    return render(request, 'index.html')

# Create your views here.
