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
    path('editprofile/', views_account.editakun, name="editprofile"),
    path('password/', views_account.change_password, name='change_password'),

    #ami umum
    # path('amiumum/', views_upmsite.AMIUmum, name='ami_umum'),

    # path('amiprodi/<int:pk>', views_upmsite.AMIProdi, name='semua_prodi'),

    # path('fileamiprodi/<int:pk>', views_upmsite.SubFileAmiProdi, name='ami_prodi_file'),

    # path('addsubfolderamiprodi/<int:pk>', views_upmsite.AddSubFolderAMIProdi01.as_view(), name="addsubfolder_amiprodi"),

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
    # folder
    path('folder/<str:kategori>/<int:pk_prodi>', viewscinta.FolderList, name="folder-list"),
    path('folder/create/<str:kategori>/<int:pk_prodi>', viewscinta.FolderCreate.as_view(), name="folder-create"),
    path('folder/update/<str:kategori>/<int:pk_prodi>', viewscinta.FolderUpdate.as_view(), name="folder-update"),
    path('folder/delete/<str:kategori>/<int:pk_prodi>', viewscinta.FolderDelete.as_view(), name="folder-delete"),

    # file
    path('file/create/<int:pk_parent>', viewscinta.FileCreate.as_view(), name="file-create"),
    path('file/update/<int:pk_parent>', viewscinta.FileUpdate.as_view(), name="file-update"),
    path('file/delete/<int:pk_parent>', viewscinta.FileDelete.as_view(), name="file-delete"),

    # sub folder 1
    path('subfolder1/<int:pk_parent>/', viewscinta.SubFolder1List, name="subfolder1-list"),
    path('subfolder1/create/<int:pk_parent>/', viewscinta.SubFolder1Create.as_view(), name="subfolder1-create"),
    path('subfolder1/update/<int:pk_parent>/', viewscinta.SubFolder1Update.as_view(), name="subfolder1-update"),
    path('subfolder1/delete/<int:pk_parent>/', viewscinta.SubFolder1Delete.as_view(), name="subfolder1-delete"),

    # sub file 1
    path('subfile1/create/<int:pk_parent>/', viewscinta.SubFile1Create.as_view(), name="subfile1-create"),
    path('subfile1/update/<int:pk_parent>/', viewscinta.SubFile1Update.as_view(), name="subfile1-update"),
    path('subfile1/delete/<int:pk_parent>/', viewscinta.SubFile1Delete.as_view(), name="subfile1-delete"),

    # subfolder 2
    path('subfolder2/<int:pk_parent>/', viewscinta.SubFolder2List, name="subfolder2-list"),
    path('subfolder2/create/<int:pk_parent>/', viewscinta.SubFolder2Create.as_view(), name="subfolder2-create"),
    path('subfolder2/update/<int:pk_parent>/', viewscinta.SubFolder2Update.as_view(), name="subfolder2-update"),
    path('subfolder2/delete/<int:pk_parent>/', viewscinta.SubFolder2Delete.as_view(), name="subfolder2-delete"),

    # sub file 2
    path('subfile2/<int:pk_parent>/', viewscinta.SubFile2List, name="subfile2-list"),
    path('subfile2/create/<int:pk_parent>', viewscinta.SubFile2Create.as_view(), name="subfile2-create"),
    path('subfile2/update/<int:pk_parent>', viewscinta.SubFile2Update.as_view(), name="subfile2-update"),
    path('subfile2/delete/<int:pk_parent>', viewscinta.SubFile2Delete.as_view(), name="subfile2-delete"),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
