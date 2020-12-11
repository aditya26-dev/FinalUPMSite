from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from Accounts.models import User 

class CreationUserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        print(fields)
        # fields = ('username', 'email', 'password1', 'password2', 'prodi', 'roles')
        
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'input', 'placeholder' : 'username'}),
            'email' : forms.EmailInput(attrs={'class': 'input', 'placeholder' : 'email'}),
            # 'password1' : forms.PasswordInput(attrs={'class': 'input', 'placeholder' : 'password'}),
            # 'password2' : forms.PasswordInput(attrs={'class': 'input', 'placeholder' : 'password'}),
            'prodi' : forms.Select(attrs={'class': 'form-control'}),
            'roles' : forms.Select(attrs={'class': 'form-control'}),
            # 'profile_picture' : forms.ImageField(),
        }