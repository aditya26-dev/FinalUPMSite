from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from upmsite import models, forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Accounts import models as models_account

@login_required(login_url='login')
def home(request):
    # query ke model Folder based on is_public = True , Category informasi umum 
    # kemudian pass konten ke main.html 
    return render(request, 'main.html')

def pengaturanakun(request):
    return render(request,"Account/Pengaturan_Akun.html")

#------ Informasi Umum-------

def BukuPanduan(request):
    bukuPanduan = models.File.objects.filter(nama_folder='1')
    print(bukuPanduan)
    context = {
        'bukupanduan': bukuPanduan
    }
    return render(request, 'InformasiUmum/BukuPanduan.html', context)

def Peraturan(request):
    peraturan = models.File.objects.filter(nama_folder='4')
    print(peraturan)
    context = {
        'peraturan': peraturan
    }
    return render(request, 'InformasiUmum/peraturan.html', context)

def InformasiUmum(request):
    roles = request.user.roles
    prodi = request.user.prodi
    semua_prodi = models_account.ProgramStudi.objects.all()
    print(semua_prodi)



    informasiUmum = models.Folder.objects.filter(kategori='Informasi Umum')
    context = {
        'informasiUmum': informasiUmum,
        'roles': roles,
        'prodi': prodi,
        'semua_prodi': semua_prodi,
    }
    return render(request, 'InformasiUmum/InformasiUmum.html', context)

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
        'pk': pk,
    }
    return render(request, 'InformasiUmum/SubInformasiUmum.html', context)
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
        'pk': pk,
    }
    return render(request, 'InformasiUmum/SubFolderInformasiUmum1.html', context)
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
    return render(request, 'InformasiUmum/SubFileInformasiUmum1.html', context)

def ABPTProdi(request):
    context = {

    }
    return render(request, 'abptprodi.html', context)

#------- CRUD Informasi UMUM ---------

class FileonFolderCreate(CreateView):
    def get_initial(self):
        pk = pkjuduldef()
        return {
            'nama_folder':pk,
        }

    template_name = "AddFile.html"
    form_class = forms.FormAddFileBukuPanduan

    def get_success_url(self):
        tes=pkjuduldef()
        print(tes)
        return reverse_lazy('sub_informasi_umum', kwargs={'pk': tes})

class UpdateFileonFolder(UpdateView):
    def get_initial(self):
        pk = pkjuduldef()
        return {
            'nama_folder':pk,
        }

    template_name = "AddFile.html"
    model = models.File
    form_class = form_class = forms.FormAddFileBukuPanduan

    def get_success_url(self):
        tes=pkjuduldef()
        print(tes)
        return reverse_lazy('sub_informasi_umum', kwargs={'pk': tes})

class DeleteFileonFolder(DeleteView):
    def get_initial(self):
        pk = pkjuduldef()
        return {
            'nama_folder':pk,
        }
    
    template_name = "DeleteConfirmation.html"
    model = models.File

    def get_success_url(self):
        tes=pkjuduldef()
        print(tes)
        return reverse_lazy('sub_informasi_umum', kwargs={'pk': tes})
    
class AddSubFolder01(CreateView):
    def get_initial(self):
        pk = pkjuduldef()
        return {
            'parent_folder':pk,
        }

    template_name = "AddSubFolder1.html"
    form_class = forms.FormAddSubFolder1

    def get_success_url(self):
        tes=pkjuduldef()
        print(tes)
        return reverse_lazy('sub_informasi_umum', kwargs={'pk': tes})

class UpdateSubFolder01(UpdateView):
    def get_initial(self):
        pk = pkjuduldef()
        return {
            'parent_folder':pk,
        }

    template_name = "AddFile.html"
    model = models.SubFolder01
    form_class = forms.FormAddSubFolder1

    def get_success_url(self):
        tes=pkjuduldef()
        print(tes)
        return reverse_lazy('sub_informasi_umum', kwargs={'pk': tes})

class DeleteSubFolder01(DeleteView):
    def get_initial(self):
        pk = pkjuduldef()
        return {
            'nama_folder':pk,
        }
    
    template_name = "DeleteConfirmation.html"
    model = models.SubFolder01

    def get_success_url(self):
        tes=pkjuduldef()
        print(tes)
        return reverse_lazy('sub_informasi_umum', kwargs={'pk': tes})

class AddSubFolder02(CreateView):
    def get_initial(self):
        pk = pkjuduldef1()
        return {
            'parent_folder':pk,
        }

    template_name = "AddSubFolder1.html"
    form_class = forms.FormAddSubFolder2

    def get_success_url(self):
        tes=pkjuduldef1()
        print(tes)
        return reverse_lazy('sub_informasi_umum', kwargs={'pk': tes})

class UpdateSubFolder02(UpdateView):
    def get_initial(self):
        pk = pkjuduldef1()
        return {
            'parent_folder':pk,
        }

    template_name = "AddFile.html"
    model = models.SubFolder02
    form_class = forms.FormAddSubFolder2

    def get_success_url(self):
        tes=pkjuduldef1()
        print(tes)
        return reverse_lazy('sub_informasi_umum', kwargs={'pk': tes})

class DeleteSubFolder02(DeleteView):
    def get_initial(self):
        pk = pkjuduldef1()
        return {
            'nama_folder':pk,
        }
    
    template_name = "DeleteConfirmation.html"
    model = models.SubFolder02

    def get_success_url(self):
        tes=pkjuduldef1()
        print(tes)
        return reverse_lazy('sub_informasi_umum', kwargs={'pk': tes})
    
def AMIUmum(request):
    files = models.File.objects.filter(nama_folder__nama_folder='AMI Umum')

    context = {
        'files': files,
    }
    return render(request, 'AMIUmum.html', context)

def AMIProdi(request):
    folder = models.SubFolder01.objects.filter(parent_folder__nama_folder = 'AMI Prodi')

    context = {
        'folder': folder,
    }
    return render(request, 'AMIProdi.html', context)
#------- Akreditasi BAN PT -------

def ABPTUmum(request):
    abptUmum = models.Folder.objects.filter(kategori='ABPT')
    print(abptUmum)
    context = {
        'abptUmum': abptUmum
    }
    return render(request, 'BANPT/BANPTumum.html', context)

pkjudulabptumum = 0
def SubFolderABPTUmum(request, pk):
    subfolderabptumum1 = models.SubFolder01.objects.filter(parent_folder__id = pk)
    filesabptumum = models.File.objects.filter(nama_folder__id = pk)
    judulabptumum = models.Folder.objects.get(id = pk)
    global pkjudulabptumum
    pkjudulabptumum = pk

    context = {
        'filesabptumum': filesabptumum,
        'subfolderabptumum1': subfolderabptumum1,
        'judulabptumum': judulabptumum,
    }
    return render(request, 'BANPT/SubBANPT.html', context)
def pkjudulabptumumdef():
    return pkjudulabptumum

