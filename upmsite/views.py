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

    prodi_terpilih = models_account.ProgramStudi.objects.filter(id=prodi.id)
    
    ami_umum = models.Folder.objects.filter(nama_prodi=None, kategori='AMI')
    abpt_umum = models.Folder.objects.filter(nama_prodi=None, kategori='ABPT')

    informasiUmum = models.Folder.objects.filter(kategori='Informasi Umum')
    context = {
        'informasiUmum': informasiUmum,
        'roles': roles,
        'prodi': prodi,
        'semua_prodi': semua_prodi,
        'prodi_terpilih': prodi_terpilih,
        'ami_umum': ami_umum,
        'abpt_umum': abpt_umum,
    }
    return render(request, 'InformasiUmum/InformasiUmum.html', context)

pkjudul = 0
def SubFolderInformasiUmum(request, pk):
    roles = request.user.roles
    prodi = request.user.prodi
    semua_prodi = models_account.ProgramStudi.objects.all()

    subfolder1 = models.SubFolder01.objects.filter(parent_folder__id = pk)
    files = models.File.objects.filter(nama_folder__id = pk)
    judul = models.Folder.objects.get(id = pk)

    global pkjudul, bagianinfoumum
    pkjudul = pk
    bagianinfoumum = 'Informasi Umum'


    print(judul.isAllowNewFolder)
    context = {
        'roles': roles,
        'prodi': prodi,
        'semua_prodi': semua_prodi,
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
    roles = request.user.roles
    prodi = request.user.prodi
    semua_prodi = models_account.ProgramStudi.objects.all()

    subfolder2 = models.SubFolder02.objects.filter(parent_folder__id = pk)
    
    pkjudul = pkjuduldef()
    judul = models.Folder.objects.get(id = pkjudul)
    
    judul1 = models.SubFolder01.objects.get(id = pk)
    global pkjudul1
    pkjudul1 = pk

    context = {
        'roles': roles,
        'prodi': prodi,
        'semua_prodi': semua_prodi,
        'subfolder2': subfolder2,
        'pkjudul': pkjudul,
        'judul': judul,
        'judul1': judul1,
        'pk': pk,
    }
    return render(request, 'InformasiUmum/SubFolderInformasiUmum1.html', context)
def pkjuduldef1():
    return pkjudul1

pkjudul2 = 0
def SubFileInformasiUmum1(request, pk):
    roles = request.user.roles
    prodi = request.user.prodi
    semua_prodi = models_account.ProgramStudi.objects.all()

    subfile2 = models.SubFile02.objects.filter(nama_folder__id = pk)
    pkjudul = pkjuduldef()
    judul = models.Folder.objects.get(id = pkjudul)

    pkjudul1 = pkjuduldef1()
    judul1 = models.SubFolder01.objects.get(id = pkjudul1)

    judul2 = models.SubFolder02.objects.get(id = pk)
    global pkjudul2
    pkjudul2 = pk

    context = {
        'roles': roles,
        'prodi': prodi,
        'semua_prodi': semua_prodi,
        'subfile2': subfile2,
        'judul': judul,
        'pkjudul': pkjudul,
        'judul1': judul1,
        'pkjudul1': pkjudul1,
        'judul2': judul2,
        'pk' : pk,
    }
    return render(request, 'InformasiUmum/SubFileInformasiUmum1.html', context)
def pkjuduldef2():
    return pkjudul2

def AMIUmum(request):
    roles = request.user.roles
    prodi = request.user.prodi
    semua_prodi = models_account.ProgramStudi.objects.all()
    files = models.File.objects.filter(nama_folder__nama_folder='AMI Umum')

    context = {
        'files': files,
        'roles': roles,
        'prodi': prodi,
        'semua_prodi': semua_prodi,
    }
    return render(request, 'AMIUmum.html', context)

pkprodi = 0
def AMIProdi(request, pk):
    roles = request.user.roles
    prodi = request.user.prodi
    semua_prodi = models_account.ProgramStudi.objects.all()

    semua_prodi_nama = models_account.ProgramStudi.objects.get(id = pk)

    semua_folder = models.SubFolder01.objects.filter(parent_folder__nama_folder = 'AMI Prodi', parent_folder__nama_prodi__id = pk)

    folder = models.Folder.objects.get(nama_prodi__id = pk)

    # global pkprodi
    # pkprodi = folder.id

    global pkprodi
    pkprodi = pk

    context = {
        'roles': roles,
        'prodi': prodi,
        'semua_prodi': semua_prodi,
        'nama_prodi': semua_prodi_nama,
        'semua_folder': semua_folder,
        'pk': pk,
    }
    return render(request, 'AMIProdi.html', context)
def datapkprodi():
    return pkprodi

def SubFileAmiProdi(request, pk):

    
    return render(request, 'SubFileAmiProdi.html', context)

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

class AddSubFolderAMIProdi01(CreateView):
    def get_initial(self):
        pk = datapkprodi()
        folder = models.Folder.objects.get(nama_prodi__id = pk)
        print(pk)
        return {
            'parent_folder': folder.id,
        }

    template_name = "AddSubFolder1.html"
    form_class = forms.FormAddSubFolder1

    def get_success_url(self):
        tes=datapkprodi()
        print(tes)
        return reverse_lazy('semua_prodi', kwargs={'pk': tes})

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
        return reverse_lazy('sub_folder_informasi_umum1', kwargs={'pk': tes})

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
        return reverse_lazy('sub_folder_informasi_umum1', kwargs={'pk': tes})

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
        return reverse_lazy('sub_folder_informasi_umum1', kwargs={'pk': tes})

class FileonFolderCreate2(CreateView):
    def get_initial(self):
        pk = pkjuduldef2()
        return {
            'nama_folder':pk,
        }

    template_name = "AddFile.html"
    form_class = forms.FormAddSubFile2

    def get_success_url(self):
        tes=pkjuduldef2()
        print(tes)
        return reverse_lazy('sub_file_informasi_umum1', kwargs={'pk': tes})

class UpdateFileonFolder2(UpdateView):
    def get_initial(self):
        pk = pkjuduldef2()
        return {
            'nama_folder':pk,
        }

    template_name = "AddFile.html"
    model = models.SubFile02
    form_class = form_class = forms.FormAddSubFile2

    def get_success_url(self):
        tes=pkjuduldef2()
        print(tes)
        return reverse_lazy('sub_file_informasi_umum1', kwargs={'pk': tes})

class DeleteFileonFolder2(DeleteView):
    def get_initial(self):
        pk = pkjuduldef2()
        return {
            'nama_folder':pk,
        }
    
    template_name = "DeleteConfirmation.html"
    model = models.SubFile02

    def get_success_url(self):
        tes=pkjuduldef2()
        print(tes)
        return reverse_lazy('sub_file_informasi_umum1', kwargs={'pk': tes})
    

#------- Akreditasi BAN PT -------

def ABPTUmum(request):
    roles = request.user.roles
    prodi = request.user.prodi
    semua_prodi = models_account.ProgramStudi.objects.all()

    abptUmum = models.Folder.objects.filter(kategori='ABPT')
    print(abptUmum)
    context = {
        'abptUmum': abptUmum,
        'roles': roles,
        'prodi': prodi,
        'semua_prodi': semua_prodi,
    }
    return render(request, 'BANPT/BANPTumum.html', context)

pkjudulabptumum = 0
def SubFolderABPTUmum(request, pk):
    roles = request.user.roles
    prodi = request.user.prodi
    semua_prodi = models_account.ProgramStudi.objects.all()

    subfolderabptumum1 = models.SubFolder01.objects.filter(parent_folder__id = pk)
    filesabptumum = models.File.objects.filter(nama_folder__id = pk)
    judulabptumum = models.Folder.objects.get(id = pk)
    global pkjudulabptumum
    pkjudulabptumum = pk

    context = {
        'roles': roles,
        'prodi': prodi,
        'semua_prodi': semua_prodi,
        'filesabptumum': filesabptumum,
        'subfolderabptumum1': subfolderabptumum1,
        'judulabptumum': judulabptumum,
    }
    return render(request, 'BANPT/SubBANPT.html', context)
    
def pkjudulabptumumdef():
    return pkjudulabptumum

