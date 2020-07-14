from django.shortcuts import render
from django.http import HttpResponse
from . models import InsertMarks
from . models import Qaa
# Create your views here.
def demo(r):
    data=InsertMarks.objects.all()
    params={'da':data}
    return render(r,'home.html',params)
def cprog(r):
    data=Qaa.objects.all()
    params={'da':data}
    return render(r,'c.html',params)

def javaprog(r):
    data=Qaa.objects.all()
    params={'da':data}
    return render(r,'java.html',params)

def pythonprog(r):
    data=Qaa.objects.all()
    params={'da':data}
    return render(r,'python.html',params)

def contact(r):
    data=Qaa.objects.all()
    params={'da':data}
    return render(r,'contact.html',params)