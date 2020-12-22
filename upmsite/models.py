from django.db import models
from Accounts.models import ProgramStudi

# Create your models here.
class Folder(models.Model):

    listKategori = (
        ('AMI', 'AMI'),
        ('ABPT', 'ABPT'),
        ('Informasi Umum', 'Informasi Umum'),
    )

    nama_folder = models.CharField(default='', max_length=256)
    nama_prodi = models.ForeignKey(ProgramStudi, on_delete=models.CASCADE, blank = True, null = True)
    kategori = models.CharField(max_length=50, choices=listKategori)
    public_status = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isAllowNewFolder = models.BooleanField(default = True)
    isAllowNewFile = models.BooleanField(default = True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return '{} ({})'.format(self.nama_folder, self.nama_prodi)

class File(models.Model):

    nama_file = models.CharField(max_length=250)
    nama_folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank = True, null = True)
    file_attachment = models.FileField(blank = True, null = True)
    public_status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
    

    def __str__(self):
        return '{} ({})'.format(self.nama_file, self.nama_folder)

class SubFolder01(models.Model):
    
    nama_folder = models.CharField(max_length=520)
    parent_folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return '{} ({})'.format(self.nama_folder, self.parent_folder)

class SubFile01(models.Model):

    nama_file = models.CharField(max_length=250)
    nama_folder = models.ForeignKey(SubFolder01, on_delete=models.CASCADE)
    file_attachment = models.FileField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return '{}'.format(self.nama_file)

class SubFolder02(models.Model):
    
    nama_folder = models.CharField(max_length=250)
    parent_folder = models.ForeignKey(SubFolder01, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return '{} ({})'.format(self.nama_folder, self.parent_folder)


class SubFile02(models.Model):

    nama_file = models.CharField(max_length=250)
    nama_folder = models.ForeignKey(SubFolder02, on_delete=models.CASCADE)
    file_attachment = models.FileField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return '{}'.format(self.nama_file)


