from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .decorators import unauthenticated_user
from .forms import CreationUserForm
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from Accounts import models


# Create your views here.
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect("Informasi_Umum")
        else :
            messages.info(request, 'Email or Password is incorrect')

    return render(request, 'Account/UPM_Login.html')

def logoutUser(request):
    logout(request)
    return redirect("login")

# @login_required(login_url='login')
def daftarakun(request):
    form = CreationUserForm()

    if request.method == 'POST':
        form = CreationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("akun")

    context = {'form' : form}

    return render(request, 'Account/Register.html', context)
    
class akun(ListView):
    model = get_user_model()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context




