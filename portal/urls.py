from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('portal', views.portal, name='portal')
]
