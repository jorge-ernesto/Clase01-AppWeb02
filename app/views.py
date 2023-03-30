from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Otra vez desde Django!')

def saludo(request):
    return render(request,'app/index.html')

def index(request,nombre):
    contexto={'nombre':nombre}
    return render(request,'app/saludo.html',contexto)

def equipo(request,num):
    contexto={'numero':num}
    return render(request,'app/hincha.html',contexto)

