from django.urls import path
from book_store.views import bookHome, details,contactUs, aboutUs,delete,search

urlpatterns = [
    path('',bookHome),
    path('details/<id>',details,name='book_store.details'),
    path('delete/<id>',delete,name='book_store.delete'),
    path('contact-us',contactUs, name='book_store.contact_us'),
    path('about-us',aboutUs, name='book_store.about_us'),
    path('<name>',search, name='book_store.search'),

]








