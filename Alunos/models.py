from django.db import models

class Curso (models.Model):
    titulo = models.CharField(
        max_length=255,
        null=False,
        blank=False)
    
    descricao = models.TextField()

class Aluno (models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
)
    
    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
)
    
    email = models.EmailField(
        max_length=50,
        null=False,
        blank=False
    )
    
    cursos = models.ManyToManyField(Curso, related_name="alunos")
    
    objetos = models.Manager()
    
