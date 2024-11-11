from django.shortcuts import render
from .models import Aluno, Curso
from django.shortcuts import get_object_or_404

def listAlunos(request):
    alunos = Aluno.objects.all().order_by("nome")
    cursos = Curso.objects.all()
    
    return render (request, 'Alunos/index.html', {'alunos': alunos, 'cursos': cursos} )

def alunosCursos(request, id):
    cursos = Curso.objects.all()
    curso = get_object_or_404(Curso, id=id)
    alunos = curso.alunos.all()
    return render(request, 'Alunos/alunos_por_curso.html', {'curso': curso, 'cursos': cursos, 'alunos': alunos})