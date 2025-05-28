from django.shortcuts import render
from django.http import HttpResponse
from .models import Manager

# Create your views here.
def me(request):
    return render(request, 'about/me.html')

def op(request):
    return render(request, 'about/op.html')

def classmates(request):
    return render(request, 'about/classmates.html')

def managers(request):
    managers_data = Manager.objects.all()
    return render(request, 'about/managers.html', {'managers': managers_data})