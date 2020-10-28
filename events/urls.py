from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_events, name='events'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
]