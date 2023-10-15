from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from accounts.forms import MyUserCreationForm
from django.contrib.auth.models import  User
from book_store.models import Book
from django.views.generic.edit import UpdateView





def login_(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('book_store.home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html',context={'form': form})



def register_(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login'))  # Change 'home' to your desired URL
    else:
        form = MyUserCreationForm()
    return render(request, 'registration.html',context={'form': form})




def logout_(request):
    logout(request)
        # return redirect('accounts.logout')
    return render(request, 'logout.html')
    



def profile_(request):
    print(request.user.id)

    if request.user != 'None':
        books = Book.objects.filter(owner=request.user.id)
        return render(request,'profile.html',context={'books':books})
    else:
        return redirect(reverse('book_store.home'))
    



class UpdateAccount(UpdateView):
    model = User
    template_name = 'update_account.html'
    fields = ['username','first_name','last_name', 'email']
    success_url = reverse_lazy('account_updated')

    def get_object(self, queryset=None):
        return self.request.user

def account_updated(request):
    return render(request, 'success_updated.html')