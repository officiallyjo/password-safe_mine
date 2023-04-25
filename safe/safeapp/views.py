from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




def home(request):
    return render(request,"safeapp/home.html")

def add(request):
    return HttpResponse('add')


def detail(request,pk):
    return HttpResponse('detail')



def delete(reques,pk):
    return HttpResponse('delete')


def update(request,pk):
    return HttpResponse('update')
