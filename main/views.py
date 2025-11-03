from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import *
from .forms import *


def index(request):
    context = {
        "now": datetime.datetime.now(),
    }
    return render(request, 'index.html', context)

def fanlar_view(request):
    # if request.method == "POST":
    #     Fan.objects.create(
    #         nom = request.POST.get("nom"),
    #         asosiy = request.POST.get("asosiy") == 'on',
    #         yonalish_id = request.POST.get("yonalish")
    #     )
    form = FanForm()
    if request.method == "POST":
        form_data = FanForm(request.POST)
        if form_data.is_valid():
            form_data.save()
        return redirect('/fanlar/')

    yonalishlar = Yonalish.objects.all()
    fanlar = Fan.objects.all()
    search = request.GET.get('search')
    if search:
        fanlar = fanlar.filter(nom__icontains=search)

    context = {
        "fanlar": fanlar,
        "search": search,
        'yonalishlar': yonalishlar,
        "form": form,
    }
    return render(request, 'fanlar.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Fan, Yonalish

def fan_update_view(request, fan_id):
    fan = get_object_or_404(Fan, id=fan_id)
    yonalishlar = Yonalish.objects.all()

    if request.method == "POST":
        fan.nom = request.POST.get("nom")
        fan.asosiy = request.POST.get("asosiy") == 'on'
        fan.yonalish_id = request.POST.get("yonalish")
        fan.save()
        return redirect('/fanlar/')

    context = {
        "fan": fan,
        "yonalishlar": yonalishlar
    }
    return render(request, 'fan_update.html', context)

def fan_delete_view(request, fan_id):
    fan = Fan.objects.get(id=fan_id)
    fan.delete()
    return redirect('/fanlar/')

def yonalishlar_view(request):
    yonalishlar = Yonalish.objects.all()
    # if request.method == "POST":
    #     Yonalish.objects.create(
    #         nom = request.POST.get("nom"),
    #         aktiv = request.POST.get("aktiv") == 'on',
    #     )
    #     return redirect('/yonalishlar/')

    form = YonalishForm()
    if request.method == "POST":
        form_data = YonalishForm(request.POST)
        if form_data.is_valid():
            form_data.save()
        return redirect('/yonalishlar/')



    context = {
        "yonalishlar": yonalishlar,
        'form': form,
    }
    return render(request, 'yonalishlar.html', context)

def yonalish_update_view(request, yonalish_id):
    yonalish = Yonalish.objects.get(id=yonalish_id)
    if request.method == "POST":
        yonalish.nom = request.POST.get("nom")
        yonalish.aktiv = request.POST.get("aktiv") == 'on'
        yonalish.save()
        return redirect('/yonalishlar/')
    context = {
        "yonalish": yonalish,
    }
    return render(request, 'yonalish_update.html', context)

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
    form = UstozForm()
    if request.method == "POST":
        form_data = UstozForm(request.POST)
        if form_data.is_valid():
            form_data.save()
        return redirect('/ustozlar/')
    fanlar = Fan.objects.all()
    ustozlar = Ustoz.objects.all()
    context = {
        "ustozlar": ustozlar,
        "form": form,
        "fanlar": fanlar,
    }
    return render(request, 'ustozlar.html', context)


def ustozlar_update_view(request, ustoz_id):
    ustoz = Ustoz.objects.get(id=ustoz_id)
    fanlar = Fan.objects.all()
    if request.method == "POST":
        ustoz.ism = request.POST.get("ism")
        ustoz.yosh = request.POST.get("yosh")
        ustoz.jins = request.POST.get("jins")
        ustoz.daraja = request.POST.get("daraja")
        ustoz.save()
        return redirect('/ustozlar/')
    context = {
        "ustoz": ustoz,
        "fanlar": fanlar,
    }
    return render(request, 'ustozlar_update.html', context)

def ustoz_delete_view(request, ustoz_id):
    ustoz = Ustoz.objects.get(id=ustoz_id)
    ustoz.delete()
    return redirect('/ustozlar/')