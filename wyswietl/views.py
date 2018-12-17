from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .forms import OdbiorcaForm
from .forms import ParametryForm
from .models import Odbiorca
from .models import Parametry
from .forms import UOAP0Form
from .models import UOAP0
from .models import UOAP2
from .forms import UOAP2Form


def index(request):
    return render_to_response('index.html')


def centrifugal_pump_form(request):
    """
        Template to P3 Project
    """
    if request.method == "POST":
       form=ParametryForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect(centrifugal_pump_result) 
    else:
        form=ParametryForm()
    return render(request,'edit.html',{'form':form})


def centrifugal_pump_result(request):
    """
        Result of P3 Project
    """
    post=Odbiorca.objects.all().last()
    parametry=Parametry.objects.all().last()
    return render(request,'test.html',{'parametry':parametry})


def electrostatic_form(request):
    """
        Form of P2 project
    """
    if request.method == "POST":
       form=UOAP2Form(request.POST)
       if form.is_valid():
            form.save()
            return redirect(electrostatic_result)
    else:
        form=UOAP2Form()
    return render(request,'uoapp2.html',{'form':form})


def electrostatic_result(request):
    """
        Result of P3 project
    """
    post = Odbiorca.objects.all().last()
    parametry = UOAP2.objects.all().last()
    return uoapp0(request,'uoap2result.html',{'uoap2':parametry})


def boiler_forms(request):
    if request.method == "POST":
       form=UOAP0Form(request.POST)
       if form.is_valid():
            form.save()
            return redirect(boiler_result)
    else:
        form=UOAP0Form()
    return render(request,'uoapp0.html',{'form':form})


def boiler_result(request):
    
     post=Odbiorca.objects.all().last()
     parametry=UOAP0.objects.all().last()
     return render(request,'test.html',{'uoap0':parametry})
