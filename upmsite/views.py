from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from upmsite import models

@login_required(login_url='login')
def home(request):
    # query ke model Folder based on is_public = True , Category informasi umum 
    # kemudian pass konten ke main.html 
    return render(request, 'main.html')

def BukuPanduan(request):
    return render(request, 'BukuPanduan.html')

def InformasiUmum(request):
    informasiUmum = models.Folder.objects.filter(kategori='Informasi Umum')
    print(informasiUmum)
    # kemudian pass konten ke main.html 
    context = {
        'informasiUmum': informasiUmum
    }
    return render(request, 'InformasiUmum.html', context)