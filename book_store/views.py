from django.shortcuts import render,redirect,get_object_or_404
from book_store.models import Book
from book_store.forms import BookForm
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from book_store.models import Book
from django.urls import reverse_lazy


class ListBooks(ListView):
    model = Book
    template_name = 'book_store/index.html'
    context_object_name = 'books'


class DetailBooks(DetailView):
    model = Book
    template_name = 'book_store/details.html'
    context_object_name = 'book'

class DeleteBooks(DeleteView):
    model = Book
    template_name = 'book_store/delete.html'
    context_object_name = 'book'
    success_url = reverse_lazy('book_store.home')



class CreateBooks(CreateView):
    model = Book
    template_name = 'book_store/add.html'
    success_url = reverse_lazy('book_store.home')
    fields = ['name','description','image','price','inStock','category']

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        if Book.objects.filter(name=name).exists():
            form.add_error('name', 'This Book is Exist!')
            return self.form_invalid(form)

        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class EditBooks(UpdateView):
    model = Book
    template_name = 'book_store/edit.html' 
    success_url = reverse_lazy('book_store.home')
    fields = ['name', 'description', 'image', 'price', 'inStock', 'category']

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        book_id = self.kwargs['pk']  

        is_exist = Book.objects.filter(name=name).exclude(id=book_id).first()

        if is_exist:
            form.add_error('name', 'This Book is Exist!')
            return self.form_invalid(form)

        form.instance.owner = self.request.user
        return super().form_valid(form)

def search(request,name):
    items = Book.objects.filter(name__icontains=name)
    return render(request,'book_store/index.html',context={'books':items})

def contactUs(request):
    return render(request,'book_store/contactUs.html')

def aboutUs(request):
    return render(request,'book_store/aboutUs.html')