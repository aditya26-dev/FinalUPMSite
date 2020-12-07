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

class FormAddFilePeraturan(ModelForm):
    class Meta:
        model = File
        fields = '__all__'

        '''
        widgets = {
            'nama_file' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'fileName'}),
            'nama_folder' : forms.HiddenInput(),
            'file_attachment' : forms.FileField(attrs={'class': 'form-control')),
            'public_status' : forms.HiddenInput()

        }
        '''
