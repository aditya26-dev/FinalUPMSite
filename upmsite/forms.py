from django.forms import ModelForm
from .models import *

class FormAddFileBukuPanduan(ModelForm):
    class Meta:
        model = File
        fields = '__all__'

        '''
        widgets = {
            'nama_file' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'fileName'}),
            'nama_folder' : forms.HiddenInput(),
            'file_attachment' : forms.FileField(upload_to='media/', attrs={'class': 'form-control')),
            'public_status' : forms.HiddenInput()

        }
        '''

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
