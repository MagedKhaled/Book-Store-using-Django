from django.urls import path
from .views import login_, logout_, register_, profile_, UpdateAccount,account_updated


urlpatterns = [
    path('login/', login_, name='login'),
    path('logout/', logout_, name='logout'),
    path('register/', register_, name='register'),
    path('profile/', profile_, name='profile'),
    path('update/<int:pk>/', UpdateAccount.as_view(), name='update_account'),
    path('success_updated/', account_updated, name='account_updated'), 



]

