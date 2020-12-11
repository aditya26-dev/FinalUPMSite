from django.forms import ModelForm
from django import forms
from .models import *

class FormAddFileBukuPanduan(ModelForm):
    class Meta:
        model = File
        fields = '__all__'

        widgets = {
            'nama_file' : forms.TextInput(attrs={'class': 'input', 'placeholder' : 'fileName'}),
            'nama_folder' : forms.Select(attrs={'class': 'form-control'}),
            'file_attachment' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'public_status' : forms.CheckboxInput()
        }

class FormAddFolder(ModelForm):
    class Meta:
        model = Folder
        fields = '__all__'
        widgets = {
            'nama_folder' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Tulis nama Folder di sini ...'}),
            'nama_prodi' : forms.Select(attrs={'class': 'form-control'}),
            'kategori' : forms.Select(attrs={'class': 'form-control'}),
            'public_status' : forms.CheckboxInput()
        }

class FormAddSubFolder1(ModelForm):
    class Meta:
        model = SubFolder01
        fields = '__all__'
        widgets = {
            'nama_folder' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Tulis nama Folder di sini ...'}),
            'parent_folder' : forms.Select(attrs={'class': 'form-control'}),
        }

class FormAddSubFolder2(ModelForm):
    class Meta:
        model = SubFolder02
        fields = '__all__'

class FormAddSubFile2(ModelForm):
    class Meta:
        model = SubFile02
        fields = '__all__'

        widgets = {
            'nama_file' : forms.TextInput(attrs={'class': 'input', 'placeholder' : 'fileName'}),
            'nama_folder' : forms.Select(attrs={'class': 'form-control'}),
            'file_attachment' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'public_status' : forms.CheckboxInput()
        }