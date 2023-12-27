from django.shortcuts import render
from django.http import HttpResponse
from . models import Todo

def say_hello(request):
    return render(request,'hello.html')

def home(request): 
    todos = Todo.objects.all()
    return render(request,'home.html',{
        'todos' : todos
    })

