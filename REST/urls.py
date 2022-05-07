"""REST URL Configuration

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
from django.urls import path
from rest_app.views import *
from rest_app.classviews import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('single-stud/<int:pk>/',single_stud, name= 'single_stud'),
    path('all-stud/', all_stud, name= 'all_stud'),
    path('create-data/', create_data, name= 'create_data'),


    # single api for CRUD operation
    path('stu_api/', stu_api, name= 'stu_api'),

    # class based
    path('stu_class_api/', StudentAPI, name= 'stu_class_api'),

]
