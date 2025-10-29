from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import *

def index(request):
    context = {
        "now": datetime.datetime.now(),
    }
    return render(request, 'index.html', context)

def fanlar_view(request):
    if request.method == "POST":
        Fan.objects.create(
            nom = request.POST.get("nom"),
            asosiy = request.POST.get("asosiy") == 'on',
            yonalish_id = request.POST.get("yonalish")
        )

    yonalishlar = Yonalish.objects.all()
    fanlar = Fan.objects.all()
    search = request.GET.get('search')
    if search:
        fanlar = fanlar.filter(nom__icontains=search)

    context = {
        "fanlar": fanlar,
        "search": search,
        'yonalishlar': yonalishlar,
    }
    return render(request, 'fanlar.html', context)

def fan_delete_view(request, fan_id):
    fan = Fan.objects.get(id=fan_id)
    fan.delete()
    return redirect('/fanlar/')

def yonalishlar_view(request):
    if request.method == "POST":
        Yonalish.objects.create(
            nom = request.POST.get("nom"),
            aktiv = request.POST.get("aktiv") == 'on',
        )
        return redirect('/yonalishlar/')


    yonalishlar = Yonalish.objects.all()
    context = {
        "yonalishlar": yonalishlar,

    }
    return render(request, 'yonalishlar.html', context)

def yonalish_delete_view(request, yonalish_id):
    yonalish = Yonalish.objects.get(id=yonalish_id)
    yonalish.delete()
    return redirect('/yonalishlar/')

def yonalish_delete_confirm_view(request, yonalish_id):
    yonalish = Yonalish.objects.get(id=yonalish_id)
    context = {
        "yonalish": yonalish,
    }
    return render(request, 'yonalish_delete_confirm.html', context)

def ustozlar_view(request):
    if request.method == "POST":
        fan_id = request.POST.get("fan")
        fan = Fan.objects.get(id=fan_id)
        Ustoz.objects.create(
            ism = request.POST.get("ism"),
            yosh = request.POST.get("yosh"),
            jins = request.POST.get("jins"),
            daraja = request.POST.get("daraja"),
            fan = fan,
        )
        return redirect('/ustozlar/')
    ustozlar = Ustoz.objects.all()
    fanlar = Fan.objects.all()

    context = {
        "ustozlar": ustozlar,
        "fanlar": fanlar,
    }
    return render(request, 'ustozlar.html', context)

def ustoz_delete_view(request, ustoz_id):
    ustoz = Ustoz.objects.get(id=ustoz_id)
    ustoz.delete()
    return redirect('/ustozlar/')