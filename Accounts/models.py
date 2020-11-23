from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class ProgramStudi(models.Model):
    nama_prodi = models.CharField(max_length=200)
    def __str__(self):
        return self.nama_prodi

class Account(models.Model):
    nama_akun = models.CharField(max_length=200)
    prodi = models.ForeignKey(ProgramStudi, models.SET_NULL, blank=True, null=True, default=None)


class User(AbstractUser):
    prodi = models.ForeignKey(ProgramStudi, models.SET_NULL, blank=True, null=True, default=None)
    role_list = (
        ('Admin', 'Admin'),
        ('Faculty Member', 'Faculty Member'),
        ('Professional Staf', 'Professional Staf')
    )
    roles = models.CharField(choices=role_list, max_length=40)

    objects = UserManager
