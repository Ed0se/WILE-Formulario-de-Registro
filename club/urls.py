from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('miembros/', views.lista_motociclistas, name='lista_motociclistas'),
    path('miembros/<int:pk>/', views.detalle_motociclista, name='detalle_motociclista'),
    path('miembros/nuevo/', views.crear_motociclista, name='crear_motociclista'),
    path('miembros/<int:pk>/editar/', views.editar_motociclista, name='editar_motociclista'),
    path('miembros/<int:pk>/baja/', views.eliminar_motociclista, name='eliminar_motociclista'),
]
