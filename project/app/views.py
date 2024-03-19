from django.shortcuts import render
from app.models import *
# Create your views here.

def home(request):
    alltodos = Todo.objects.all()
    d = {'alltodos':alltodos}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        if title and desc:
            TO = Todo(name=title,desc=desc)
            TO.save()
    return render(request, 'home.html',d)