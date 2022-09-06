from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    path('upload/register',register,name='register'),
    path('upload/',signin,name='signin'),
    path('upload/signin/signin',signin,name='signin/signin'),
]

