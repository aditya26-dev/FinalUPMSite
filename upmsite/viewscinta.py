from django.shortcuts import render, redirect, get_object_or_404
from upmsite import models, forms
from Accounts import models as models_account
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def FolderList(request, kategori, pk_prodi):
    roles = request.user.roles
    prodi = request.user.prodi
    semua_prodi = models_account.ProgramStudi.objects.all()

    semua_prodi = models_account.ProgramStudi.objects.all()
    
    informasiUmum = models.Folder.objects.filter(kategori=kategori, nama_prodi__id=pk_prodi)
    selected_prodi = models_account.ProgramStudi.objects.get(id=pk_prodi)


    #rename Kategori
    label = kategori
    if kategori == "ABPT":
        label = "Akreditasi BAN PT"

    context = {
        'pk_prodi': pk_prodi,
        'label': label,
        'kategori': kategori,
        'informasiUmum': informasiUmum,
        'roles': roles,
        'prodi': selected_prodi.nama_prodi,
        'semua_prodi': semua_prodi,
    }
    return render(request, 'Akreditasi/FolderList.html', context)

def SubFolder1List(request, pk):
    roles = request.user.roles
    prodi = request.user.prodi
    semua_prodi = models_account.ProgramStudi.objects.all()

    subfolder1 = models.SubFolder01.objects.filter(parent_folder__id = pk)
    files = models.File.objects.filter(nama_folder__id = pk)
    folder = models.Folder.objects.get(id = pk)
    kategori = folder.kategori


    context = {
        'kategori': kategori,
        'roles': roles,
        'prodi': prodi,
        'semua_prodi': semua_prodi,
        'files': files,
        'subfolder1': subfolder1,
        'judul': folder,
        'pk': pk,
    }
    return render(request, 'Akreditasi/SubFolder1List.html', context)

class FolderCreate(CreateView):
    def get_initial(self):
        pk = self.kwargs.get('pk_prodi')
        kategori = self.kwargs.get('kategori')
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
        prodi_name = models_account.ProgramStudi.objects.get(id=pk)
        context["prodi_name"] = prodi_name.nama_prodi

        return context