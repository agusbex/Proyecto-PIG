from django.urls import path, re_path , include
from django.contrib.auth import views as auth_views
from . import views 
from django.conf import settings
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
     
    path("accounts/login/", auth_views.LoginView.as_view(template_name="web/login.html"), name="login"),
    path("accounts/logout/", views.user_logout, name="logout"),
    path("accounts/password_reset/", auth_views.PasswordResetView.as_view(template_name="web/password_reset.html"), name="password_reset"),
    
    path('saludar/<str:nombre>', views.saludar, name='saludar'),
    path('contacto/', views.contacto, name='contacto'),
    path('seguimiento/', views.seguimiento, name='seguimiento'),
    path('administracion/', views.administracion, name='administracion'),
    path('editar_orden/<int:id>/', views.editar_orden, name='editar_orden'),
    path('eliminar_orden/<int:id>/', views.eliminar_orden, name='eliminar_orden'),
    path('crear_orden/', views.crear_orden, name='crear_orden'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
