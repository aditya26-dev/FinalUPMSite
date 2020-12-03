from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from upmsite import models, forms

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

def Peraturan(request):
    peraturan = models.File.objects.filter(nama_folder='4')
    print(peraturan)
    context = {
        'peraturan': peraturan
    }
    return render(request, 'peraturan.html', context)

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

def AddFileBukuPanduan(request):

    form = forms.FormAddFileBukuPanduan()
    context = {
        'form': form,
    }

    if request.method == 'POST':
            post = request.POST
            nama_file = post['nama_file']
            nama_folder = models.Folder.objects.get(nama_folder = 'Buku Panduan')
            file_attachment = post['file_attachment']
            public_status = True
            new_file = models.File(
                nama_file = nama_file,
                nama_folder = nama_folder,
                file_attachment = file_attachment,
                public_status = public_status,
            )
            new_file.save()
            return redirect('Buku_Panduan')

    return render(request, 'AddFile.html', context)

def UpdateFileBukuPanduan(request, id): 

    context ={} 
  
    obj = get_object_or_404(models.File, id = id) 
  
    form = forms.FormAddFileBukuPanduan(request.POST or None, instance = obj) 
  
    if request.method == 'POST':
            post = request.POST
            obj.nama_file = post['nama_file']
            nama_folder = models.Folder.objects.get(nama_folder = 'Buku Panduan')
            if post['file_attachment'] == "":
                obj.file_attachment = obj.file_attachment
                print("kosong")
                print(post['file_attachment'])
            else:
                obj.file_attachment = post['file_attachment']
                print("isi")
                print(post['file_attachment'])
            public_status = True
            obj.save()
            return redirect('Buku_Panduan')
  
    context["form"] = form 
  
    return render(request, "AddFile.html", context)

def DeleteFileBukuPanduan(request, id): 
    context ={} 
  
    obj = get_object_or_404(models.File, id = id) 
  
  
    if request.method =="POST": 
        obj.delete() 
        return redirect('Buku_Panduan')
  
    return render(request, "DeleteConfirmation.html", context) 


def AddFilePeraturan(request):

    form = forms.FormAddFilePeraturan()
    context = {
        'form': form,
    }

    if request.method == 'POST':
            post = request.POST
            nama_file = post['nama_file']
            nama_folder = models.Folder.objects.get(nama_folder = 'Peraturan-Peraturan')
            file_attachment = post['file_attachment']
            public_status = True
            new_file = models.File(
                nama_file = nama_file,
                nama_folder = nama_folder,
                file_attachment = file_attachment,
                public_status = public_status,
            )
            new_file.save()
            return redirect('Buku_Panduan')

    return render(request, 'AddFile.html', context)

def UpdateFilePeraturan(request, id): 

    obj = get_object_or_404(models.File, id = id) 
  

    form = forms.FormAddFilePeraturan(request.POST or None, instance = obj) 
    context = {
        'form': form,
    }
  
    if form.is_valid(): 
        form.save() 
        return redirect('Buku_Panduan') 
  
  
    return render(request, "AddFile.html", context)

def DeleteFilePeraturan(request, id): 
    context ={} 
  
    obj = get_object_or_404(models.File, id = id) 
  
  
    if request.method =="POST": 
        obj.delete() 
        return redirect('Buku_Panduan')
  
    return render(request, "DeleteConfirmation.html", context) 