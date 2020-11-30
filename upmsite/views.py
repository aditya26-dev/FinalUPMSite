from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from upmsite import models

@login_required(login_url='login')
def home(request):
    # query ke model Folder based on is_public = True , Category informasi umum 
    # kemudian pass konten ke main.html 
    return render(request, 'main.html')

def BukuPanduan(request):
    bukuPanduan = models.File.objects.filter(nama_folder='1')
    print(bukuPanduan)
    context = {
        'bukupanduan': bukuPanduan
    }
    return render(request, 'BukuPanduan.html', context)

def InformasiUmum(request):
    #link = request.
    informasiUmum = models.Folder.objects.filter(kategori='Informasi Umum')
    print(informasiUmum)
    # kemudian pass konten ke main.html 
    context = {
        'informasiUmum': informasiUmum
    }
    return render(request, 'InformasiUmum.html', context)

def SubFolderInformasiUmum(request, pk):
    files = models.File.objects.filter(nama_folder__id = pk)
    #informasiUmum = models.Folder.objects.filter(kategori='Informasi Umum')
    #print(informasiUmum)
    # kemudian pass konten ke main.html 
    context = {
        'files': files,
    }
    return render(request, 'SubInformasiUmum.html', context)