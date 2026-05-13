from django import forms
from .models import Motociclista


class MotociclistaForm(forms.ModelForm):
    class Meta:
        model = Motociclista
        exclude = ['fecha_registro', 'fecha_actualizacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre(s)'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido Paterno'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido Materno'}),
            'apodo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu apodo en el club'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tipo_sangre': forms.Select(attrs={'class': 'form-control'}),
            'curp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CURP', 'maxlength': '18'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(+52) 000 000 0000'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'estado_republica': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Dirección completa'}),
            'marca_moto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Harley-Davidson'}),
            'modelo_moto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Sportster 1200'}),
            'año_moto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 2020', 'min': 1950, 'max': 2025}),
            'cilindrada': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 1200'}),
            'color_moto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Color'}),
            'placa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ABC-123-D'}),
            # Vehículo extra
            'vehiculo_modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo del vehículo'}),
            'vehiculo_placa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Placa del vehículo'}),
            # Experiencia
            'años_experiencia': forms.Select(attrs={'class': 'form-control'}),
            'tiene_licencia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'numero_licencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de licencia'}),
            'contacto_emergencia_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'contacto_emergencia_telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'contacto_emergencia_parentesco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Esposa, Hermano'}),
            # Salud
            'grupo_sanguineo': forms.Select(attrs={'class': 'form-control'}),
            'es_alergico': forms.Select(attrs={'class': 'form-control'}),
            'alergico_especifique': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especifique...'}),
            'padecimiento_fisico': forms.Select(attrs={'class': 'form-control'}),
            'padecimiento_especifique': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especifique...'}),
            'tratamiento_medico': forms.Select(attrs={'class': 'form-control'}),
            'tratamiento_especifique': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especifique...'}),
            'toma_medicamento': forms.Select(attrs={'class': 'form-control'}),
            'medicamento_especifique': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especifique...'}),
            'forma_suministro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indique la forma de suministro'}),
            'seguro_medico': forms.Select(attrs={'class': 'form-control'}),
            'seguro_especifique': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especifique...'}),
            # Documentos
            'documentos': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': '.pdf,.jpg,.jpeg,.png'}),
            'foto_identificacion': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': '.pdf,.jpg,.jpeg,.png'}),
            # Legal
            'acepta_responsabilidad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'acepta_tratamiento_datos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'acepta_privacidad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'acepta_permiso_fotos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            # Firma
            'firma': forms.HiddenInput(attrs={'id': 'firma-data'}),
            # Estado
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'notas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Información adicional...'}),
        }
