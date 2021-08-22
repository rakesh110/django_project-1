"""Django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from enroll import views as enroll_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.user_login, name='login'),
    path('logout/', user_views.user_logout, name='logout'),

    path('blog/', include('blog.urls')),
    path('registration/', enroll_views.registration, name='registration'),
    path('showformdata/',enroll_views.showformdata,name='showformdata'),
    path('export_users_xls/', enroll_views.export_users_xls, name="export-excel"),
    path('send_sms/', enroll_views.send_sms, name="send_sms"),


    
]

