# ☠ Hell's Angels MC — Sistema de Registro
## README de Instalación y Uso

---

## 🔧 Requisitos
- Python 3.10+
- pip

---

## 🚀 Instalación (5 pasos)

```bash
# 1. Entra al directorio del proyecto
cd hells_angels

# 2. Instala Django
pip install -r requirements.txt

# 3. Aplica las migraciones (crea la base de datos SQLite)
python manage.py migrate

# 4. Crea tu usuario administrador
python manage.py createsuperuser
# (Ingresa usuario, email y contraseña cuando te pida)

# 5. Inicia el servidor
python manage.py runserver
```

---

## 🌐 URLs del Sistema

| URL | Descripción |
|-----|-------------|
| `http://127.0.0.1:8000/` | **Home** — Información del club, estadísticas |
| `http://127.0.0.1:8000/login/` | Login del sistema |
| `http://127.0.0.1:8000/miembros/` | Lista de motociclistas (requiere login) |
| `http://127.0.0.1:8000/miembros/nuevo/` | Registrar nuevo miembro |
| `http://127.0.0.1:8000/miembros/<id>/` | Ver detalle de miembro |
| `http://127.0.0.1:8000/miembros/<id>/editar/` | Editar miembro |
| `http://127.0.0.1:8000/miembros/<id>/baja/` | Dar de baja |
| `http://127.0.0.1:8000/admin/` | Panel de administración Django |

---

## 📋 Funcionalidades

### ✅ CRUD Completo
- **Alta**: Formulario completo de inscripción con datos personales, moto, experiencia y contacto de emergencia
- **Baja**: Confirmación antes de eliminar permanentemente
- **Editar**: Todos los campos modificables
- **Ver**: Vista detallada de cada motociclista

### ✅ Home con info del club
- Estadísticas en tiempo real (total miembros, activos)
- Historia e información del club
- Estética Hell's Angels

### ✅ Autenticación
- Login requerido para gestión de miembros
- Home público (visible sin login)
- Logout disponible en navbar

### ✅ Filtros y búsqueda
- Búsqueda por nombre, apodo, email o marca de moto
- Filtro por estado (activo/inactivo/suspendido)

---

## 🏗️ Estructura del Proyecto

```
hells_angels/
├── manage.py
├── requirements.txt
├── hells_angels/          # Configuración Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── club/                  # App principal
│   ├── models.py          # Modelo Motociclista
│   ├── views.py           # Lógica CRUD
│   ├── forms.py           # Formulario de registro
│   ├── urls.py            # Rutas de la app
│   └── admin.py           # Admin Django
├── templates/club/        # Templates HTML
│   ├── base.html          # Layout base con navbar/footer
│   ├── home.html          # Página principal
│   ├── login.html         # Pantalla de login
│   ├── lista.html         # Lista de miembros
│   ├── formulario.html    # Alta/edición
│   ├── detalle.html       # Vista detallada
│   └── confirmar_baja.html
└── static/
    ├── css/estilo.css     # Estilos Hell's Angels
    └── js/main.js         # JavaScript frontend
```

---

## 🎨 Estética
- **Paleta**: Negro profundo + Rojo sangre + Dorado
- **Tipografía**: Metal Mania (títulos) + Oswald + Rajdhani
- **Estilo**: Dark industrial, inspirado en hells-angels.com

---

## 📝 Datos del Formulario de Registro
Basado en la plantilla Tesalia MotoClub (Jotform):

**Personales**: Nombre, apellidos, apodo, fecha de nacimiento, tipo de sangre, CURP  
**Contacto**: Email, teléfono, ciudad, estado, dirección  
**Moto**: Marca, modelo, año, cilindrada, color, placas  
**Experiencia**: Años de experiencia, licencia, número de licencia  
**Emergencia**: Nombre, teléfono y parentesco del contacto  
**Club**: Estado (activo/inactivo/suspendido), notas

---

☠ *"When we do right, nobody remembers. When we do wrong, nobody forgets."* ☠
