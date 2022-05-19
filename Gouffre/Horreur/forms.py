from django.forms import ModelForm
from . import models
from .models import Films
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import NumberInput

class FilmForm(ModelForm):
    class Meta:
        model = models.Films
        fields = ('nom', 'date_de_sortie', 'realisateur', 'resume')
        labels = {
            'nom' : _('Nom du film'),
            'date_de_sortie' : _('date_de_sortie'),
            'realisateur' : _('Realisateur du film'),
            'resume': _('Résumé')
        }

