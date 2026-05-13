from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Motociclista
from .forms import MotociclistaForm


def home(request):
    total = Motociclista.objects.count()
    activos = Motociclista.objects.filter(estado='activo').count()
    context = {
        'total_miembros': total,
        'miembros_activos': activos,
    }
    return render(request, 'club/home.html', context)


@login_required
def lista_motociclistas(request):
    query = request.GET.get('q', '')
    estado = request.GET.get('estado', '')
    motociclistas = Motociclista.objects.all()

    if query:
        motociclistas = motociclistas.filter(
            Q(nombre__icontains=query) |
            Q(apellido_paterno__icontains=query) |
            Q(apodo__icontains=query) |
            Q(email__icontains=query) |
            Q(marca_moto__icontains=query)
        )
    if estado:
        motociclistas = motociclistas.filter(estado=estado)

    context = {
        'motociclistas': motociclistas,
        'query': query,
        'estado_filtro': estado,
        'total': motociclistas.count(),
    }
    return render(request, 'club/lista.html', context)


@login_required
def detalle_motociclista(request, pk):
    motociclista = get_object_or_404(Motociclista, pk=pk)
    return render(request, 'club/detalle.html', {'motociclista': motociclista})


@login_required
def crear_motociclista(request):
    if request.method == 'POST':
        form = MotociclistaForm(request.POST, request.FILES)
        if form.is_valid():
            motociclista = form.save()
            messages.success(request, f'¡Hermano {motociclista.nombre} {motociclista.apellido_paterno} registrado en el club!')
            return redirect('lista_motociclistas')
    else:
        form = MotociclistaForm()
    return render(request, 'club/formulario.html', {'form': form, 'titulo': 'Nuevo Prospecto', 'accion': 'Registrar'})


@login_required
def editar_motociclista(request, pk):
    motociclista = get_object_or_404(Motociclista, pk=pk)
    if request.method == 'POST':
        form = MotociclistaForm(request.POST, request.FILES, instance=motociclista)
        if form.is_valid():
            form.save()
            messages.success(request, f'Datos de {motociclista.nombre} actualizados.')
            return redirect('lista_motociclistas')
    else:
        form = MotociclistaForm(instance=motociclista)
    return render(request, 'club/formulario.html', {'form': form, 'titulo': 'Editar Miembro', 'accion': 'Guardar Cambios', 'motociclista': motociclista})


@login_required
def eliminar_motociclista(request, pk):
    motociclista = get_object_or_404(Motociclista, pk=pk)
    if request.method == 'POST':
        nombre = motociclista.nombre_completo()
        motociclista.delete()
        messages.success(request, f'{nombre} ha sido dado de baja del club.')
        return redirect('lista_motociclistas')
    return render(request, 'club/confirmar_baja.html', {'motociclista': motociclista})
