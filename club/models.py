from django.db import models

TIPO_SANGRE_CHOICES = [
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'),
    ('O+', 'O+'), ('O-', 'O-'),
]

ESTADO_CHOICES = [
    ('activo', 'Activo'),
    ('inactivo', 'Inactivo'),
    ('suspendido', 'Suspendido'),
]

EXPERIENCIA_CHOICES = [
    ('menos_1', 'Menos de 1 año'),
    ('1_3', '1 a 3 años'),
    ('3_5', '3 a 5 años'),
    ('5_10', '5 a 10 años'),
    ('mas_10', 'Más de 10 años'),
]

SI_NO_CHOICES = [
    ('', 'Seleccionar'),
    ('si', 'Sí'),
    ('no', 'No'),
]

GRUPO_SANGUINEO_CHOICES = [
    ('', 'Seleccionar'),
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'),
    ('O+', 'O+'), ('O-', 'O-'),
]


class Motociclista(models.Model):
    # Datos personales
    nombre = models.CharField(max_length=100, verbose_name='Nombre(s)')
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='Apellido Materno', blank=True)
    apodo = models.CharField(max_length=100, verbose_name='Apodo / Alias', blank=True)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    tipo_sangre = models.CharField(max_length=5, choices=TIPO_SANGRE_CHOICES, verbose_name='Tipo de Sangre')
    curp = models.CharField(max_length=18, verbose_name='CURP', blank=True)
    
    # Contacto
    email = models.EmailField(verbose_name='Correo Electrónico', unique=True)
    telefono = models.CharField(max_length=15, verbose_name='Teléfono')
    ciudad = models.CharField(max_length=100, verbose_name='Ciudad')
    estado_republica = models.CharField(max_length=100, verbose_name='Estado')
    direccion = models.TextField(verbose_name='Dirección', blank=True)
    
    # Motocicleta
    marca_moto = models.CharField(max_length=100, verbose_name='Marca de la Motocicleta')
    modelo_moto = models.CharField(max_length=100, verbose_name='Modelo')
    año_moto = models.IntegerField(verbose_name='Año')
    cilindrada = models.CharField(max_length=50, verbose_name='Cilindrada (cc)')
    color_moto = models.CharField(max_length=50, verbose_name='Color')
    placa = models.CharField(max_length=20, verbose_name='Placas')

    # Vehículo extra
    vehiculo_modelo = models.CharField(max_length=100, verbose_name='Vehículo Modelo', blank=True)
    vehiculo_placa = models.CharField(max_length=20, verbose_name='Vehículo Placa', blank=True)
    
    # Experiencia
    años_experiencia = models.CharField(max_length=20, choices=EXPERIENCIA_CHOICES, verbose_name='Años de Experiencia')
    tiene_licencia = models.BooleanField(default=True, verbose_name='¿Cuenta con Licencia?')
    numero_licencia = models.CharField(max_length=50, verbose_name='Número de Licencia', blank=True)
    
    # Contacto de emergencia
    contacto_emergencia_nombre = models.CharField(max_length=200, verbose_name='Nombre del Contacto de Emergencia')
    contacto_emergencia_telefono = models.CharField(max_length=15, verbose_name='Teléfono de Emergencia')
    contacto_emergencia_parentesco = models.CharField(max_length=50, verbose_name='Parentesco')

    # Registro de Salud
    grupo_sanguineo = models.CharField(max_length=5, choices=GRUPO_SANGUINEO_CHOICES, verbose_name='Grupo Sanguíneo', blank=True)
    es_alergico = models.CharField(max_length=2, choices=SI_NO_CHOICES, verbose_name='¿Es alérgico a?', blank=True)
    alergico_especifique = models.CharField(max_length=200, verbose_name='Especifique alergia', blank=True)
    padecimiento_fisico = models.CharField(max_length=2, choices=SI_NO_CHOICES, verbose_name='¿Sufre algún padecimiento físico?', blank=True)
    padecimiento_especifique = models.CharField(max_length=200, verbose_name='Especifique padecimiento', blank=True)
    tratamiento_medico = models.CharField(max_length=2, choices=SI_NO_CHOICES, verbose_name='¿Está bajo algún tratamiento médico?', blank=True)
    tratamiento_especifique = models.CharField(max_length=200, verbose_name='Especifique tratamiento', blank=True)
    toma_medicamento = models.CharField(max_length=2, choices=SI_NO_CHOICES, verbose_name='¿Toma algún medicamento?', blank=True)
    medicamento_especifique = models.CharField(max_length=200, verbose_name='Especifique medicamento', blank=True)
    forma_suministro = models.CharField(max_length=200, verbose_name='Forma de suministro', blank=True)
    seguro_medico = models.CharField(max_length=2, choices=SI_NO_CHOICES, verbose_name='¿Posee seguro médico?', blank=True)
    seguro_especifique = models.CharField(max_length=200, verbose_name='Especifique seguro', blank=True)

    # Documentos y Soportes
    documentos = models.FileField(upload_to='documentos/', verbose_name='Adjuntar Documentos', blank=True, null=True)
    foto_identificacion = models.FileField(upload_to='identificaciones/', verbose_name='Adjuntar Foto de Identificación', blank=True, null=True)

    # Aspecto Legal
    acepta_responsabilidad = models.BooleanField(default=False, verbose_name='Acepto la Liberación de Responsabilidad Social')
    acepta_tratamiento_datos = models.BooleanField(default=False, verbose_name='Acepto el Tratamiento de Datos')
    acepta_privacidad = models.BooleanField(default=False, verbose_name='Acepto la Política de Privacidad')
    acepta_permiso_fotos = models.BooleanField(default=False, verbose_name='Acepto el Permiso de Fotografías')

    # Firma
    firma = models.TextField(verbose_name='Firma de Conformidad', blank=True, help_text='Datos de firma en formato base64')
    
    # Estado en el club
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo', verbose_name='Estado')
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')
    notas = models.TextField(blank=True, verbose_name='Notas Adicionales')

    class Meta:
        verbose_name = 'Motociclista'
        verbose_name_plural = 'Motociclistas'
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} ({self.apodo or 'Sin apodo'})"

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}".strip()
