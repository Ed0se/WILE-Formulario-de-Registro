from django.contrib import admin
from .models import Motociclista


@admin.register(Motociclista)
class MotociclistaAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'apodo', 'email', 'ciudad', 'marca_moto', 'estado', 'fecha_registro']
    list_filter = ['estado', 'años_experiencia', 'tipo_sangre']
    search_fields = ['nombre', 'apellido_paterno', 'apodo', 'email']
    readonly_fields = ['fecha_registro', 'fecha_actualizacion']
