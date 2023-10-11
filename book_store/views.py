from django.shortcuts import render
from django.http import HttpResponse
from book_store.models import Book
# Create your views here.


def bookHome(request): 
    return render(request,'book_store/index.html',context={'books':Book.objects.all()})

def details(request,id):
    return render(request,'book_store/details.html',context={'book':Book.objects.filter(id=id)[0]})

def delete(request,id):
    Book.objects.filter(id=id).delete()
    return render(request,'book_store/index.html',context={'books':Book.objects.all()})

def contactUs(request):
    return render(request,'book_store/contactUs.html')

def aboutUs(request):
    return render(request,'book_store/aboutUs.html')

def search(request,name):
    items = Book.objects.filter(name__icontains=name)
    print(items)
    print(name)
    return render(request,'book_store/index.html',context={'books':items})
