from django.shortcuts import render,redirect,reverse
from category.models import Category
from book_store.models import Book
# Create your views here.


def home(request):
    return render(request,'category/home.html')

def details(request,name):
    print(name)
    if name != 'None':
        print('test')
        category = Category.objects.get(name=name)
        books = Book.objects.filter(category=category.id)
        return render(request,'category/details.html',context={'category':category,'books':books})
    else:
        return redirect(reverse('book_store.home'))



