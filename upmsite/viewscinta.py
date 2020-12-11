from django.shortcuts import render, redirect, get_object_or_404
from upmsite import models, forms
from Accounts import models as models_account

def FolderHandler(request, kategori, pk_prodi):
    roles = request.user.roles
    prodi = request.user.prodi
    semua_prodi = models_account.ProgramStudi.objects.all()

    semua_prodi = models_account.ProgramStudi.objects.all()
    
    informasiUmum = models.Folder.objects.filter(kategori=kategori, nama_prodi__id=pk_prodi)
    selected_prodi = models_account.ProgramStudi.objects.get(id=pk_prodi)


    #rename Kategori
    if kategori == "ABPT":
        kategori = "Akreditasi BAN PT"
    context = {
        'kategori': kategori,
        'informasiUmum': informasiUmum,
        'roles': roles,
        'prodi': selected_prodi.nama_prodi,
        'semua_prodi': semua_prodi,
    }
    return render(request, 'Akreditasi/FolderList.html', context)