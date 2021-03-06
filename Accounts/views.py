from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
# from django.contrib.auth.models import User
from .decorators import unauthenticated_user
from .forms import CreationUserForm, CustomUserChangeForm
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
            return redirect("home")
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

def editakun(request):
    user = request.user

    form = CustomUserChangeForm(instance=user)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("Informasi_Umum")

    context = {'form' : form}

    return render(request, 'Account/Edit_Akun.html', context)
    
class akun(ListView):
    model = get_user_model()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Yey kamu berhasil mengubah password!')
            return redirect('editprofile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Account/change_password.html', {
        'form': form
    })



