from django.shortcuts import render, redirect, get_object_or_404
from upmsite import models, forms
from Accounts import models as models_account
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
import datetime
from django.utils import timezone

data_pk_prodi = 0
def FolderList(request, kategori, pk_prodi):
    roles = request.user.roles
    prodi = request.user.prodi

    semua_prodi = models_account.ProgramStudi.objects.all()
    prodi_terpilih = models_account.ProgramStudi.objects.filter(id=prodi.id)
    ami_umum = models.Folder.objects.filter(nama_prodi=None, kategori='AMI')
    abpt_umum = models.Folder.objects.filter(nama_prodi=None, kategori='ABPT')

    global data_pk_prodi
    data_pk_prodi = pk_prodi
    if kategori == 'Informasi Umum':
        kategori = kategori
        informasiUmum = models.Folder.objects.filter(kategori=kategori)

        print(informasiUmum[0].created_at)

        print(timezone.localtime(informasiUmum[0].updated_at))
        now = datetime.datetime.now()
        nowtimezone = timezone.now()

        print(informasiUmum)

        time = timezone.localtime(informasiUmum[0].updated_at)
        p_informasiumum = Paginator(informasiUmum, 5)
        page_number = request.GET.get('page')
        
        jumlah_halaman = []

        for x in range(1, p_informasiumum.num_pages+1):
            jumlah_halaman.append(x)

        context = {
            'pk_prodi': pk_prodi,
            'roles': roles,
            'prodi': prodi,
            'pages': p_informasiumum.get_page(page_number),
            'jumlah_halaman': jumlah_halaman,
        }
    else:
        semua_prodi = models_account.ProgramStudi.objects.all()
        
        informasiUmum = models.Folder.objects.filter(kategori=kategori, nama_prodi__id=pk_prodi)
        selected_prodi = models_account.ProgramStudi.objects.get(id=pk_prodi)

        label = kategori
        if kategori == "ABPT":
            label = "ABPT"
        elif kategori == "AMI":
            label = "AMI"

        context = {
            'pk_prodi': pk_prodi,
            'label': label,
            'informasiUmum': informasiUmum,
            'roles': roles,
            'prodi': selected_prodi.nama_prodi,
        }
    context1 = {
        'kategori': kategori,
        'ami_umum': ami_umum,
        'abpt_umum': abpt_umum,
        'semua_prodi': semua_prodi,
        'prodi_terpilih': prodi_terpilih,
    }
    return render(request, 'Akreditasi/FolderList.html', {**context , **context1})
def data_pk_prodidef():
    return data_pk_prodi

data_pk_prodi1 = 0
def SubFolder1List(request, pk_parent):
    roles = request.user.roles
    prodi = request.user.prodi

    semua_prodi = models_account.ProgramStudi.objects.all()
    prodi_terpilih = models_account.ProgramStudi.objects.filter(id=prodi.id)
    ami_umum = models.Folder.objects.filter(nama_prodi=None, kategori='AMI')
    abpt_umum = models.Folder.objects.filter(nama_prodi=None, kategori='ABPT')

    link1 = data_pk_prodidef()

    global data_pk_prodi1
    data_pk_prodi1 = pk_parent

    amiumum = models.Folder.objects.get(id=pk_parent)
    if amiumum.kategori == 'AMI':
        amiumum_folders = models.SubFolder01.objects.filter(parent_folder__id = pk_parent)
        amiumum_files = models.File.objects.filter(nama_folder__id = pk_parent)
        kategori = amiumum.kategori

        print(amiumum.nama_prodi)

        context = {
            'bagian': amiumum.nama_prodi,
            'kategori': kategori,
            'folder': amiumum_folders,
            'files': amiumum_files,
            'pk_parent': pk_parent,
            'link1': link1,
            'judul': amiumum,
        }
    elif amiumum.kategori == 'ABPT':
        abptumum_files = models.File.objects.filter(nama_folder__id = pk_parent)
        abptumum_folders = models.SubFolder01.objects.filter(parent_folder__id = pk_parent)
        kategori = amiumum.kategori


        context = {
            'bagian': amiumum.nama_prodi,
            'kategori': kategori,
            'folder': abptumum_folders,
            'files': abptumum_files,
            'pk_parent': pk_parent,
            'link1': link1,
            'judul': amiumum,
        }
    elif amiumum.kategori == 'Informasi Umum':
        subfolder1 = models.SubFolder01.objects.filter(parent_folder__id = pk_parent)
        files = models.File.objects.filter(nama_folder__id = pk_parent)
        folder = models.Folder.objects.get(id = pk_parent)
        kategori = folder.kategori

        context = {
            'kategori': kategori,
            'files': files,
            'subfolder1': subfolder1,
            'judul': folder,
            'pk_parent': pk_parent,
            'link1': link1,
        }
    else:
        subfolder1 = models.SubFolder01.objects.filter(parent_folder__id = pk_parent)
        files = models.File.objects.filter(nama_folder__id = pk_parent)
        folder = models.Folder.objects.get(id = pk_parent)
        kategori = folder.kategori

        context = {
            'kategori': kategori,
            'files': files,
            'subfolder1': subfolder1,
            'judul': folder,
            'pk_parent': pk_parent,
            'link1': link1,
        }

    context1 = {
        'roles': roles,
        'ami_umum': ami_umum,
        'abpt_umum': abpt_umum,
        'semua_prodi': semua_prodi,
        'prodi_terpilih': prodi_terpilih,
    }
    return render(request, 'Akreditasi/SubFolder1List.html', {**context , **context1})
def data_pk_prodidef1():
    return data_pk_prodi1

data_pk_prodi2 = 0
def SubFolder2List(request, pk_parent):
    roles = request.user.roles
    prodi = request.user.prodi

    semua_prodi = models_account.ProgramStudi.objects.all()
    prodi_terpilih = models_account.ProgramStudi.objects.filter(id=prodi.id)
    ami_umum = models.Folder.objects.filter(nama_prodi=None, kategori='AMI')
    abpt_umum = models.Folder.objects.filter(nama_prodi=None, kategori='ABPT')

    subfolder1 = models.SubFolder02.objects.filter(parent_folder__id = pk_parent)
    files = models.SubFile01.objects.filter(nama_folder__id = pk_parent)
    folder = models.SubFolder01.objects.get(id = pk_parent)

    kategori = folder.parent_folder.kategori

    link1 = data_pk_prodidef()
    link2 = data_pk_prodidef1()
    linksubfolder1 = models.Folder.objects.get(id = link2)

    print(folder.parent_folder.nama_prodi)

    global data_pk_prodi2
    data_pk_prodi2 = pk_parent

    context = {
        'bagian': folder.parent_folder.nama_prodi,
        'kategori': kategori,
        'roles': roles,
        'semua_prodi': semua_prodi,
        'files': files,
        'subfolder1': subfolder1,
        'judul': folder,
        'pk_parent': pk_parent,
        'link1': link1,
        'link2': link2,
        'linksubfolder1': linksubfolder1,
    }
    context1 = {
        'ami_umum': ami_umum,
        'abpt_umum': abpt_umum,
        'semua_prodi': semua_prodi,
        'prodi_terpilih': prodi_terpilih,
    }
    return render(request, 'Akreditasi/SubFolder2List.html', {**context , **context1})
def data_pk_prodidef2():
    return data_pk_prodi2

def SubFile2List(request, pk_parent):
    roles = request.user.roles
    prodi = request.user.prodi

    semua_prodi = models_account.ProgramStudi.objects.all()
    prodi_terpilih = models_account.ProgramStudi.objects.filter(id=prodi.id)
    ami_umum = models.Folder.objects.filter(nama_prodi=None, kategori='AMI')
    abpt_umum = models.Folder.objects.filter(nama_prodi=None, kategori='ABPT')

    subfolder1 = models.SubFolder02.objects.filter(parent_folder__id = pk_parent)
    files = models.SubFile02.objects.filter(nama_folder__id = pk_parent)
    folder = models.SubFolder02.objects.get(id = pk_parent)

    kategori = folder.parent_folder.parent_folder.kategori

    link1 = data_pk_prodidef()
    link2 = data_pk_prodidef1()
    linksubfolder1 = models.Folder.objects.get(id = link2)
    link3 = data_pk_prodidef2()
    linksubfolder2 = models.SubFolder01.objects.get(id = link3)

    context = {
        'bagian': folder.parent_folder.parent_folder.nama_prodi,
        'kategori': kategori,
        'roles': roles,
        'semua_prodi': semua_prodi,
        'files': files,
        'subfolder1': subfolder1,
        'judul': folder,
        'pk_parent': pk_parent,
        'link1': link1,
        'link2': link2,
        'linksubfolder1': linksubfolder1,
        'link3': link3,
        'linksubfolder2': linksubfolder2,
    }
    context1 = {
        'ami_umum': ami_umum,
        'abpt_umum': abpt_umum,
        'semua_prodi': semua_prodi,
        'prodi_terpilih': prodi_terpilih,
    }
    return render(request, 'Akreditasi/SubFile2List.html', {**context , **context1})

# _______ CRUD FOLDER

class FolderCreate(CreateView):
    def get_initial(self):
        pk = self.kwargs.get('pk_prodi')
        kategori = self.kwargs.get('kategori')

        if kategori == 'Informasi Umum':
            return {
                'kategori': kategori,
            }
        else:
            parent_prodi = models_account.ProgramStudi.objects.get(id=pk)
            return {
                'kategori': kategori,
                'nama_prodi': pk,
            }

    template_name = "Akreditasi/FolderAdd.html"
    form_class = forms.FormAddFolder

    def get_success_url(self):
        pk = self.kwargs.get('pk_prodi')
        kategori = self.kwargs.get('kategori')
        return reverse_lazy('folder-list', kwargs={'pk_prodi': pk, 'kategori': kategori})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_prodi')
        kategori = self.kwargs.get('kategori')

        if kategori == 'Informasi Umum':
            context["prodi_name"] = kategori
            return context
        else:
            prodi_name = models_account.ProgramStudi.objects.get(id=pk)
            context["prodi_name"] = prodi_name.nama_prodi
            return context
 
class FolderUpdate(UpdateView):
    def get_object(self):
        id_ = self.kwargs.get('pk_prodi')
        return get_object_or_404(models.Folder, id=id_)

    template_name = "Akreditasi/FolderAdd.html"
    model = models.Folder
    form_class = forms.FormAddFolder
 
    def get_success_url(self):
        pk = self.kwargs.get('pk_prodi')
        prodi = models.Folder.objects.get(id=pk)
        kategori = self.kwargs.get('kategori')
        if kategori == 'Informasi Umum':
            return reverse_lazy('folder-list', kwargs={'pk_prodi': pk, 'kategori': kategori}) 
        else:
            return reverse_lazy('folder-list', kwargs={'pk_prodi': prodi.nama_prodi.id, 'kategori': kategori})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kategori = self.kwargs.get('kategori')
        pk = self.kwargs.get('pk_prodi')
        if kategori == 'Informasi Umum':
            context["prodi_name"] = kategori
            return context
        else:
            prodi_name = models.Folder.objects.get(id=pk)
            context["prodi_name"] = prodi_name.nama_prodi
            return context

class FolderDelete(DeleteView):
    def get_object(self):
        id_ = self.kwargs.get('pk_prodi')
        print(id_)
        return get_object_or_404(models.Folder, id=id_)

    template_name = "Akreditasi/FolderDelete.html"
    model = models.Folder
    form_class = forms.FormAddFolder

    def get_success_url(self):
        pk = self.kwargs.get('pk_prodi')
        prodi = models.Folder.objects.get(id=pk)
        kategori = self.kwargs.get('kategori')
        if kategori == 'Informasi Umum':
            return reverse_lazy('folder-list', kwargs={'pk_prodi': pk, 'kategori': kategori}) 
        else:
            return reverse_lazy('folder-list', kwargs={'pk_prodi': prodi.nama_prodi.id, 'kategori': kategori})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kategori = self.kwargs.get('kategori')
        pk = self.kwargs.get('pk_prodi')
        if kategori == 'Informasi Umum':
            context["prodi_name"] = kategori
            return context
        else:
            prodi_name = models.Folder.objects.get(id=pk)
            context["prodi_name"] = prodi_name.nama_prodi
            return context

# _______ CRUD FILE

class FileCreate(CreateView):
    def get_initial(self):
        pk = self.kwargs.get('pk_parent')

        return {
            'nama_folder': pk,
        }

    template_name = "Akreditasi/FolderAdd.html"
    form_class = forms.FormAddFile

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        kategori = self.kwargs.get('kategori')
        return reverse_lazy('subfolder1-list', kwargs={'pk_parent': pk})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        prodi_name = models.Folder.objects.get(id=pk)
        context["prodi_name"] = prodi_name
        return context

class FileUpdate(UpdateView):
    def get_object(self):
        id_ = self.kwargs.get('pk_parent')
        return get_object_or_404(models.File, id=id_)

    template_name = "Akreditasi/FolderAdd.html"
    model = models.File
    form_class = forms.FormAddFile

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        folder = models.File.objects.get(id=pk)
        kategori = self.kwargs.get('kategori')
        return reverse_lazy('subfolder1-list', kwargs={'pk_parent': folder.nama_folder.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        prodi_name = models.File.objects.get(id=pk)
        context["prodi_name"] = prodi_name.nama_folder
        return context

class FileDelete(DeleteView):
    def get_object(self):
        id_ = self.kwargs.get('pk_parent')
        print(id_)
        return get_object_or_404(models.File, id=id_)

    template_name = "Akreditasi/FolderDelete.html"
    model = models.File
    form_class = forms.FormAddFile

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        folder = models.File.objects.get(id=pk)
        kategori = self.kwargs.get('kategori')
        return reverse_lazy('subfolder1-list', kwargs={'pk_parent': folder.nama_folder.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        prodi_name = models.File.objects.get(id=pk)
        context["prodi_name"] = prodi_name.nama_folder
        return context

# _______ CRUD SUB FOLDER 1

class SubFolder1Create(CreateView):
    def get_initial(self):
        pk = self.kwargs.get('pk_parent')
        parent_folder = models.Folder.objects.get(id=pk)

        return {
            'parent_folder': parent_folder,
        }

    template_name = "Akreditasi/FolderAdd.html"
    form_class = forms.FormAddSubFolder1

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        return reverse_lazy('subfolder1-list', kwargs={'pk_parent': pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        folder = models.Folder.objects.get(id=pk)
        context["prodi_name"] = folder.nama_folder
        return context

class SubFolder1Update(UpdateView):
    def get_object(self):
        id_ = self.kwargs.get('pk_parent')
        return get_object_or_404(models.SubFolder01, id=id_)

    template_name = "Akreditasi/FolderAdd.html"
    model = models.SubFolder01
    form_class = forms.FormAddSubFolder1

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFolder01.objects.get(id=pk)
        return reverse_lazy('subfolder1-list', kwargs={'pk_parent': folder.parent_folder.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFolder01.objects.get(id=pk)
        context["prodi_name"] = folder.nama_folder
        return context

class SubFolder1Delete(DeleteView):
    def get_object(self):
        id_ = self.kwargs.get('pk_parent')
        return get_object_or_404(models.SubFolder01, id=id_)

    template_name = "Akreditasi/FolderDelete.html"
    model = models.SubFolder01
    form_class = forms.FormAddSubFolder1

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFolder01.objects.get(id=pk)
        return reverse_lazy('subfolder1-list', kwargs={'pk_parent': folder.parent_folder.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFolder01.objects.get(id=pk)
        context["prodi_name"] = folder.nama_folder
        return context

# _______ CRUD SUB FILE 1

class SubFile1Create(CreateView):
    def get_initial(self):
        pk = self.kwargs.get('pk_parent')

        return {
            'nama_folder': pk,
        }

    template_name = "Akreditasi/FolderAdd.html"
    form_class = forms.FormAddSubFile1

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        kategori = self.kwargs.get('kategori')
        return reverse_lazy('subfolder2-list', kwargs={'pk_parent': pk})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        prodi_name = models.SubFolder01.objects.get(id=pk)
        context["prodi_name"] = prodi_name
        return context

class SubFile1Update(UpdateView):
    def get_object(self):
        id_ = self.kwargs.get('pk_parent')
        print(id_)
        return get_object_or_404(models.SubFile01, id=id_)

    template_name = "Akreditasi/FolderAdd.html"
    form_class = forms.FormAddSubFile1

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFile01.objects.get(id=pk)
        kategori = self.kwargs.get('kategori')
        return reverse_lazy('subfolder2-list', kwargs={'pk_parent': folder.nama_folder.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFile01.objects.get(id=pk)
        context["prodi_name"] = folder.nama_file
        return context

class SubFile1Delete(DeleteView):
    def get_object(self):
        id_ = self.kwargs.get('pk_parent')
        print(id_)
        return get_object_or_404(models.SubFile01, id=id_)

    template_name = "Akreditasi/FolderDelete.html"
    form_class = forms.FormAddSubFile1

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFile01.objects.get(id=pk)
        kategori = self.kwargs.get('kategori')
        return reverse_lazy('subfolder2-list', kwargs={'pk_parent': folder.nama_folder.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFile01.objects.get(id=pk)
        context["prodi_name"] = folder.nama_file
        return context

# _______ CRUD SUB FOLDER 2

class SubFolder2Create(CreateView):
    def get_initial(self):
        pk = self.kwargs.get('pk_parent')
        parent_folder = models.SubFolder01.objects.get(id=pk)

        return {
            'parent_folder': parent_folder,
        }

    template_name = "Akreditasi/FolderAdd.html"
    form_class = forms.FormAddSubFolder2

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        return reverse_lazy('subfolder2-list', kwargs={'pk_parent': pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFolder01.objects.get(id=pk)
        context["prodi_name"] = folder.nama_folder
        return context

class SubFolder2Update(UpdateView):
    def get_object(self):
        id_ = self.kwargs.get('pk_parent')
        return get_object_or_404(models.SubFolder02, id=id_)

    template_name = "Akreditasi/FolderAdd.html"
    model = models.SubFolder02
    form_class = forms.FormAddSubFolder2

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        prodi = models.SubFolder02.objects.get(id=pk)
        return reverse_lazy('subfolder2-list', kwargs={'pk_parent': prodi.parent_folder.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFolder02.objects.get(id=pk)
        context["prodi_name"] = folder.nama_folder
        return context

class SubFolder2Delete(DeleteView):
    def get_object(self):
        id_ = self.kwargs.get('pk_parent')
        return get_object_or_404(models.SubFolder02, id=id_)

    template_name = "Akreditasi/FolderDelete.html"
    model = models.SubFolder02
    form_class = forms.FormAddSubFolder2

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        prodi = models.SubFolder02.objects.get(id=pk)
        return reverse_lazy('subfolder2-list', kwargs={'pk_parent': prodi.parent_folder.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFolder02.objects.get(id=pk)
        context["prodi_name"] = folder.nama_folder
        return context

# _______ CRUD SUB FILE 2

class SubFile2Create(CreateView):
    def get_initial(self):
        pk = self.kwargs.get('pk_parent')

        return {
            'nama_folder': pk,
        }

    template_name = "Akreditasi/FolderAdd.html"
    form_class = forms.FormAddSubFile2

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        kategori = self.kwargs.get('kategori')
        return reverse_lazy('subfile2-list', kwargs={'pk_parent': pk})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        prodi_name = models.SubFolder02.objects.get(id=pk)
        context["prodi_name"] = prodi_name
        return context

class SubFile2Update(UpdateView):
    def get_object(self):
        id_ = self.kwargs.get('pk_parent')
        return get_object_or_404(models.SubFile02, id=id_)

    template_name = "Akreditasi/FolderAdd.html"
    form_class = forms.FormAddSubFile2

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFile02.objects.get(id=pk)
        kategori = self.kwargs.get('kategori')
        return reverse_lazy('subfile2-list', kwargs={'pk_parent': folder.nama_folder.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFile02.objects.get(id=pk)
        context["prodi_name"] = folder.nama_file
        return context

class SubFile2Delete(DeleteView):
    def get_object(self):
        id_ = self.kwargs.get('pk_parent')
        return get_object_or_404(models.SubFile02, id=id_)

    template_name = "Akreditasi/FolderDelete.html"
    form_class = forms.FormAddSubFile2

    def get_success_url(self):
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFile02.objects.get(id=pk)
        kategori = self.kwargs.get('kategori')
        return reverse_lazy('subfile2-list', kwargs={'pk_parent': folder.nama_folder.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk_parent')
        folder = models.SubFile02.objects.get(id=pk)
        context["prodi_name"] = folder.nama_file
        return context