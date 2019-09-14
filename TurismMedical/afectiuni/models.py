from django.db import models

# Create your models here.
class StatiuniBalneare(models.Model):
    nume = models.CharField(blank=True, null=True,max_length=100)
    judet = models.CharField(blank=True, null=True,max_length=100)

    def __str__(self):
        template = '{0.nume} {0.judet}'
        return template.format(self)

class Afectiuni(models.Model):
    clasificare = models.CharField(blank=True, null=True,max_length=200)
    DecontatCNAS = models.BooleanField(default=False)
    StatiuneTratament = models.ManyToManyField(StatiuniBalneare, through='AfectiuniStatiuni')
    def __str__(self):
        template = '{0.clasificare} {0.DecontatCNAS}'
        return template.format(self)

class ConsultatieMedicala(models.Model):
    cosnsultatieMedicala = models.CharField(blank=True, null=True, max_length=100)
    cosnsultatieControl = models.BooleanField(default=False)
    afectiune = models.ForeignKey(Afectiuni, on_delete='cascade')
    def __str__(self):
        template = '{0.cosnsultatieMedicala} {0.cosnsultatieControl}'
        return template.format(self)

class AfectiuniStatiuni(models.Model):
    afectiune = models.ForeignKey(Afectiuni, related_name='afectiune',on_delete='cascade')
    statiune = models.ForeignKey(StatiuniBalneare, related_name='statiune',on_delete='cascade')

    def __str__(self):
        template = '{0.afectiune} {0.statiune}'
        return template.format(self)

class BazaTratament(models.Model):
    procedura = models.CharField(blank=True, null=True,max_length=100)
    statiune = models.ForeignKey(StatiuniBalneare,on_delete='cascade')
    def __str__(self):
        template = '{0.procedura}'
        return template.format(self)

class Cazare(models.Model):
    nume = models.CharField(blank=True, null=True, max_length=100)
    rating = models.CharField(blank=True, null=True, max_length=100)
    website = models.CharField(blank=True, null=True, max_length=100)
    statiune = models.ForeignKey(StatiuniBalneare,on_delete='cascade')
    def __str__(self):
        template = '{0.nume} {0.rating} {0.website}'
        return template.format(self)
class Proceduri(models.Model):
    nume = models.CharField(blank=True, null=True, max_length=300)
    def __str__(self):
        template = '{0.nume}'
        return template.format(self)
