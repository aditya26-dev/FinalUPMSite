from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from Accounts import views as views_account
from upmsite import views as views_upmsite
from Accounts.views import akun
from upmsite import viewscinta


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_account.loginPage, name="landingPage"),
    #account 

    path('login/',views_account.loginPage, name="login"),
    path('logout/', views_account.logoutUser, name="logout"),
    path('register/', views_account.daftarakun, name="register"),
    path('akun/', akun.as_view(), name='akun'),
    path('settinguser/', views_upmsite.pengaturanakun, name="pengaturan_Akun"),

    #ami umum
    path('amiumum/', views_upmsite.AMIUmum, name='ami_umum'),

    path('amiprodi/<int:pk>', views_upmsite.AMIProdi, name='semua_prodi'),

    path('fileamiprodi/<int:pk>', views_upmsite.SubFileAmiProdi, name='ami_prodi_file'),

    path('addsubfolderamiprodi/<int:pk>', views_upmsite.AddSubFolderAMIProdi01.as_view(), name="addsubfolder_amiprodi"),

    #upm site 
    path('home/', views_upmsite.home, name="home"),

    #----- INFORMASI UMUM -------
    path('bukupanduan/', views_upmsite.BukuPanduan, name="Buku_Panduan"),
    path('peraturan/', views_upmsite.Peraturan, name="Peraturan"),
    path('informasiumum/', views_upmsite.InformasiUmum, name="Informasi_Umum"),
    path('subinformasiumum/<int:pk>/', views_upmsite.SubFolderInformasiUmum, name="sub_informasi_umum"),
    path('subfolderinformasiumum1/<int:pk>/', views_upmsite.SubFolderInformasiUmum1, name="sub_folder_informasi_umum1"),
    path('subfileinformasiumum1/<int:pk>/', views_upmsite.SubFileInformasiUmum1, name="sub_file_informasi_umum1"),

    #------ AKREDITASI BAN PT ------
    path('abptumum/', views_upmsite.ABPTUmum, name="ABPT_Umum"),
    path('subabptumum/<int:pk>/', views_upmsite.SubFolderABPTUmum, name="sub_ABPT_Umum"),

    path('abpt/prodi', views_upmsite.ABPTProdi , name="ABPT_Prodi"),

    # ____________ RESET PASSWORD ____________

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="Account/UPM_Reset_Password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="Account/UPM_Reset_Password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="Account/UPM_Reset_Password_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="Account/UPM_Reset_Password_done.html"), name="password_reset_complete"),


    path('addfile_bukupanduan/<int:pk>', views_upmsite.FileonFolderCreate.as_view(), name="AddFile_BukuPanduan"),
    path('updatefile_bukupanduan/<int:pk>', views_upmsite.UpdateFileonFolder.as_view(), name="UpdateFile_BukuPanduan"),
    path('deletefile_bukupanduan/<int:pk>', views_upmsite.DeleteFileonFolder.as_view(), name="DeleteFile_BukuPanduan"),

    path('addsubfolder01/<int:pk>', views_upmsite.AddSubFolder01.as_view(), name="AddSubFolder_01"),
    path('update_subfolder01/<int:pk>', views_upmsite.UpdateSubFolder01.as_view(), name="UpdateSubFolder_01"),
    path('delete_subfolder01/<int:pk>', views_upmsite.DeleteSubFolder01.as_view(), name="DeleteSubFolder_01"),

    path('addsubfolder02/<int:pk>', views_upmsite.AddSubFolder02.as_view(), name="AddSubFolder_02"),
    path('update_subfolder02/<int:pk>', views_upmsite.UpdateSubFolder02.as_view(), name="UpdateSubFolder_02"),
    path('delete_subfolder02/<int:pk>', views_upmsite.DeleteSubFolder02.as_view(), name="DeleteSubFolder_02"),

    path('addfile_subfile02/<int:pk>', views_upmsite.FileonFolderCreate2.as_view(), name="AddSubFile_02"),
    path('updatefile_subfile02/<int:pk>', views_upmsite.UpdateFileonFolder2.as_view(), name="UpdateSubFile_02"),
    path('deletefile_subfile02/<int:pk>', views_upmsite.DeleteFileonFolder2.as_view(), name="DeleteSubFile_02"),

    #new handler by mata
    path('folder/<str:kategori>/<int:pk_prodi>', viewscinta.FolderHandler, name="folder-handler"),


    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
