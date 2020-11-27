from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from Accounts import views as views_account
from upmsite import views as views_upmsite


urlpatterns = [
    path('admin/', admin.site.urls),
    #account 

    path('login/',views_account.loginPage, name="login"),
    path('logout/', views_account.logoutUser, name="logout"),

    #upm site 
    path('home/', views_upmsite.home, name="home"),

    # ____________ RESET PASSWORD ____________

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="UPM_Reset_Password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="UPM_Reset_Password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="UPM_Reset_Password_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="UPM_Reset_Password_done.html"), name="password_reset_complete"),
]
