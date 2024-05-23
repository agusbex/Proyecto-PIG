from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('seguimiento/', views.seguimiento, name='seguimiento'),
    path('admin/', views.admin_login, name='admin_login'),
    path('administracion/', views.administracion, name='administracion'),
]