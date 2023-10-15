from django.urls import path
from category.views import home,details



urlpatterns = [
    path('home/',home,name='category.home'),
    path('details/<name>',details,name='category.details'),

]








