from django.shortcuts import render,redirect
from.models import *
from.forms import *
def home(request):
    data = Home.objects.all

    return render(request,'home.html',{"data":data})


def other(request):
    return render(request,'other.html')


def form(request):
    if request.method=='POST':
        form = HomeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HomeForm()


    return render(request,'form.html',{"form":form})


def math(request):
    data = request.POST.get('name')
    data = data[::-1]
    return render(request,'math.html',{'data':data})
