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
    informasiUmum = models.Folder.objects.filter(kategori='Informasi Umum')
    print(informasiUmum)
    context = {
        'informasiUmum': informasiUmum
    }
    return render(request, 'InformasiUmum.html', context)

pkjudul = 0
def SubFolderInformasiUmum(request, pk):
    subfolder1 = models.SubFolder01.objects.filter(parent_folder__id = pk)
    files = models.File.objects.filter(nama_folder__id = pk)
    judul = models.Folder.objects.get(id = pk)
    global pkjudul
    pkjudul = pk

    context = {
        'files': files,
        'subfolder1': subfolder1,
        'judul': judul,
    }
    return render(request, 'SubInformasiUmum.html', context)
def pkjuduldef():
    return pkjudul

pkjudul1 = 0
def SubFolderInformasiUmum1(request, pk):
    subfolder2 = models.SubFolder02.objects.filter(parent_folder__id = pk)
    
    pkjudul = pkjuduldef()
    judul = models.Folder.objects.get(id = pkjudul)
    
    judul1 = models.SubFolder01.objects.get(id = pk)
    global pkjudul1
    pkjudul1 = pk

    context = {
        'subfolder2': subfolder2,
        'pkjudul': pkjudul,
        'judul': judul,
        'judul1': judul1,
    }
    return render(request, 'SubFolderInformasiUmum1.html', context)
def pkjuduldef1():
    return pkjudul1

def SubFileInformasiUmum1(request, pk):
    subfile2 = models.SubFile02.objects.filter(nama_folder__id = pk)
    pkjudul = pkjuduldef()
    judul = models.Folder.objects.get(id = pkjudul)

    pkjudul1 = pkjuduldef1()
    judul1 = models.SubFolder01.objects.get(id = pkjudul1)

    judul2 = models.SubFolder02.objects.get(id = pk)

    context = {
        'subfile2': subfile2,
        'judul': judul,
        'pkjudul': pkjudul,
        'judul1': judul1,
        'pkjudul1': pkjudul1,
        'judul2': judul2,
    }
    return render(request, 'SubFileInformasiUmum1.html', context)