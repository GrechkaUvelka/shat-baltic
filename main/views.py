from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.core.mail import send_mail, BadHeaderError


def index(request):
    return render(request, "index.html")

def send(request):
    email = request.POST.get('email')
    s_name = request.POST.get('s_name')
    name = request.POST.get('name')
    tel = request.POST.get('tel')
    date = request.POST.get('date')
    time = request.POST.get('time')
    num = request.POST.get('num')

    if s_name and name and tel and email and date and time and num:
        body = s_name + " " + name + "\nТелефон: " + tel + "\nДата и время " + date + " " + time + "\n" + "Количество человек: " + num + "\nПочта: " + email
        send_mail('Бронирование', body, email, ["shatbaltic39@gmail.com"], fail_silently=False)
        return render(request, 'success.html')
    else:
        return render(request, "fail.html")
