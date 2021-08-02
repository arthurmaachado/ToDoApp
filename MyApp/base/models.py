from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarefa(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    titulo = models.CharField(max_length=255)
    descriçao = models.TextField(null=True,blank=True)
    completa = models.BooleanField(default=False)
    criada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['criada']
