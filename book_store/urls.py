from django.urls import path
from book_store.views import ListBooks, DetailBooks,DeleteBooks, CreateBooks,EditBooks, contactUs, aboutUs, search
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',ListBooks.as_view(),name='book_store.home'),
    path('details/<int:pk>',DetailBooks.as_view(),name='book_store.details'),
    path('delete/<int:pk>',login_required(DeleteBooks.as_view()),name='book_store.delete'),
    path('add',login_required(CreateBooks.as_view()), name='book_store.add'),
    path('edit/<int:pk>',login_required(EditBooks.as_view()),name='book_store.edit'),
    path('contact-us',contactUs, name='book_store.contact_us'),
    path('about-us',aboutUs, name='book_store.about_us'),
    path('search/<name>',search, name='book_store.search'),


]








