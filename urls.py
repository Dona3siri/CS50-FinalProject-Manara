from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('resources/', views.resources, name='resources'),
    path('create/', views.create_initiative, name='create_initiative'),
    path('delete/<int:initiative_id>/', views.delete_initiative, name='delete_initiative'),
    path('resources/', views.resources, name='resources'),
    path('initiative/<int:initiative_id>/', views.initiative_detail, name='initiative_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
