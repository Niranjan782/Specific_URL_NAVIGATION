from django.shortcuts import render

# Create your views here.

def signup(request):
    return render(request,'signup.html')

def coming(request):
    return render(request,'coming.html')