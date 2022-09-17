from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def bosh_sahifa(request):
    return render(request, 'asosiy.html')

def mashq(request):
    data = {
        'ism':'Xusniddin',
        'names':["Ali", "Bahrom", "Javlon", "Avaz", "Kozim"]
    }
    return render(request, 'mashq.html', data)

def hamma_talabalar(request):
    if request.method == 'POST':
        if request.POST.get('bt') == 'on':
            natija = True
        else:
            natija = False
        Student.objects.create(
            ism = request.POST.get('name'),
            jins = request.POST.get('gender'),
            kitob_soni = request.POST.get('books'),
            bitiruvchi = natija
        )
        return redirect('/students/')
    soz = request.GET.get('q_sozi')
    if soz is None:
        s = Student.objects.all()
    else:
        s = Student.objects.filter(ism__contains=soz)
    data = {
        'studentlar':s
    }
    return render(request, 'students.html', data)

def talaba(request, son):
    data = {
        "student":Student.objects.get(id=son)
    }
    return render(request, 'mashq/student.html', data)

def talaba_ochir(request, son):
    Student.objects.get(id=son).delete()
    return redirect('/students/')

def talaba_tasdiqlash(request, son):
    data = {
    'talaba' : Student.objects.get(id=son)
    }
    return render(request, 'talaba_ochir.html', data)

def hamma_kitoblar(request):
    if request.method == 'POST':
        son = request.POST.get('muallifi')
        m = Muallif.objects.get(id=son)
        Kitob.objects.create(
            nom = request.POST.get('nomi'),
            sahifa = request.POST.get('sahifasi'),
            janr = request.POST.get('janri'),
            muallif = m
        )
        return redirect('/books/')
    data = {
        'mualliflar':Muallif.objects.all(),
        "kitoblar":Kitob.objects.all()
    }
    return render(request, 'books.html', data)

def student_tahrirlash(request, son):
    if request.method == 'POST':
        if request.POST.get('bitiradi') is None:
            n = False
        else:
            n = True
        Student.objects.filter(id=son).update(
            ism = request.POST.get('ismi'),
            bitiruvchi = n,
            kitob_soni = request.POST.get('k_soni')
        )
        return redirect('/students/')
    data = {
        'student':Student.objects.get(id=son)
    }
    return render(request, 'student-edit.html', data)




