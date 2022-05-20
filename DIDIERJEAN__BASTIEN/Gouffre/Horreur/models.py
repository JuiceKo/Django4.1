from django.db import models

class  Films(models.Model):
    nom = models.CharField(max_length=30, blank=False)
    date_de_sortie = models.DateField(blank=True)
    realisateur = models.CharField(max_length=30)
    resume = models.TextField(blank=True)

    def __str__(self):
        chaine = f"{self.nom} réalisé par {self.realisateur} en {self.date_de_sortie} "
        return chaine

    def dico(self):
        return {"nom": self.nom, "realisateur": self.realisateur, "date_de_sortie": self.date_de_sortie, "resume": self.resume}


# Create your models here.
