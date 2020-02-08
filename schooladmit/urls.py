"""schooladmit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from application import views
from accounts import views as accounts_view
from result import views as result_view

from django.conf import settings
from django.urls import path, include, re_path 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.home,name='home'),
    path('signup/',accounts_view.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    
    re_path(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
    re_path(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),

    path('apply/',views.apply,name='apply'),
    path('show_applicants/',views.show_applicants,name='show_applicants'),
    path('payment/',result_view.payment,name='payment'),

    path('ajax/validate_contact_no/',views.validate_contact_no,name='validate_contact_no'),
    path('contact/',views.contact,name='contact'),
    path('apply/done/',views.apply_done,name='apply_done'),
    path('pdf/',result_view.GeneratePdf),

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)