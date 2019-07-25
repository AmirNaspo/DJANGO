from django.db import models
import uuid
import os
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length= 100)
    dt_criacao = models.DateTimeField(auto_now_add = True)
    def __str__ (self):
        return self.nome


class empregado (models.Model):
    Nome = models.CharField(max_length= 200)
    Area = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    Observacoes = models.TextField(null = True, blank = True)
    Foto = models.FileField(upload_to="images/")
    def __str__ (self):
        return self.Nome

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Area = models.ForeignKey(Categoria, on_delete = models.CASCADE, null = True)
    Foto = models.FileField(default = 'default.jpg',upload_to="images/%Y/%m/%d/")
    Nome = models.CharField(default = 'default', max_length= 200)
    Observacoes = models.TextField(default = 'default', null = True, blank = True)
    def __str__ (self):
        return f'{self.user.username}Profile'

class Nutri (models.Model):
    numIng = models.CharField(max_length=120)
    nomeIng = models.CharField(max_length=120)
    umidade = models.FloatField(blank = True)
    energiaKCal = models.CharField(max_length=120, blank = True)
    energiaKJ = models.CharField(max_length=120, blank = True)
    proteina = models.CharField(max_length=120, blank = True)
    lipideos = models.CharField(max_length=120, blank = True)
    colesterol = models.CharField(max_length=120, blank = True)
    carboidrato = models.CharField(max_length=120, blank = True)
    fibraAlimentar = models.CharField(max_length=120, blank = True)
    cinzas = models.CharField(max_length=120, blank = True)
    calcio = models.CharField(max_length=120, blank = True)
    magnesio = models.CharField(max_length=120, blank = True)
    manganes = models.CharField(max_length=120, blank = True)
    fosforo = models.CharField(max_length=120,blank = True)
    ferro = models.CharField(max_length=120, blank = True)
    sodio = models.CharField(max_length=120, blank = True)
    potassio = models.CharField(max_length=120, blank = True)
    cobre =models.CharField(max_length=120, blank = True)
    zinco = models.CharField(max_length=120, blank = True)
    retinol = models.CharField(max_length=120, blank = True)
    RE = models.CharField(max_length=120,blank = True)
    RAE = models.CharField(max_length=120, blank = True)
    tiamina =models.CharField(max_length=120, blank = True)
    riboflavina = models.CharField(max_length=120, blank = True)
    piridoxina = models.CharField(max_length=120, blank = True)
    niacina = models.CharField(max_length=120, blank = True)
    vitaminaC = models.CharField(max_length=120, blank = True)
    Q1 = models.CharField(max_length=120, blank = True)
    DS1 = models.CharField(max_length=120, blank = True)
    DZ1 = models.CharField(max_length=120, blank = True)
    V1 = models.CharField(max_length=120, blank = True)
    DZDNS = models.CharField(max_length=120, blank = True)
    DZTNT = models.CharField(max_length=120, blank = True)
    V4 = models.CharField(max_length=120, blank = True)
    V5 = models.CharField(max_length=120, blank = True)
    VD5 = models.CharField(max_length=120, blank = True)
    VD6 = models.CharField(max_length=120, blank = True)
    DZ1t = models.CharField(max_length=120, blank = True)
    DZ2t = models.CharField(max_length=120, blank = True)


    def __str__ (self):
        return (self.nomeIng)

class pont (models.Model):
    ColdCall = models.BooleanField(default=False)
    LALA = models.BooleanField(default=False)
    pCC = models.IntegerField (null = True, blank = True)
    def clean_ColdCall(self):
        ColdCall = self.cleaned_data['ColdCall']
        if not ColdCall:
                pCC = models.IntegerField (default = 20,null = True, blank = True)
        return yes_no
    #def __str__ (self):
     #   return self.ColdCall