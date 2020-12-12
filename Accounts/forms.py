from .models import *
from django.forms import ModelForm
from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from Accounts.models import User 

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from .models import CustomUser


class CreationUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreationUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'prodi', 'roles')
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'username'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'email'}),
            'password1' : forms.PasswordInput(attrs={'class': 'input', 'placeholder' : 'password'}),
            'password2' : forms.PasswordInput(attrs={'class': 'input', 'placeholder' : 'password'}),
            'prodi' : forms.Select(attrs={'class': 'form-control'}),
            'roles' : forms.Select(attrs={'class': 'form-control'}),
            'profile_picture' : forms.ImageField(),
        }

class CustomUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

    class Meta(UserChangeForm):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture')
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'username'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'email'}),
            'profile_picture' : forms.FileInput(),
        }

# class CreationUserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
#         print(fields)
#         # fields = ('username', 'email', 'password1', 'password2', 'prodi', 'roles')
        
#         widgets = {
#             'username' : forms.TextInput(attrs={'class': 'input', 'placeholder' : 'username'}),
#             'email' : forms.EmailInput(attrs={'class': 'input', 'placeholder' : 'email'}),
#             # 'password1' : forms.PasswordInput(attrs={'class': 'input', 'placeholder' : 'password'}),
#             # 'password2' : forms.PasswordInput(attrs={'class': 'input', 'placeholder' : 'password'}),
#             'prodi' : forms.Select(attrs={'class': 'form-control'}),
#             'roles' : forms.Select(attrs={'class': 'form-control'}),
#             # 'profile_picture' : forms.ImageField(),
#         }