from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'login.html')


def nike(request):
    return render(request,'nike.html')