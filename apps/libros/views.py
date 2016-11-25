from django.views.generic import TemplateView, ListView
from django.shortcuts import render, get_object_or_404, redirect,render_to_response
from .models import Libro
from .forms import LibroForm
from apps.autores.models import Autor

def libro_lista(request):
    libros = Libro.objects.all
    return render(request, 'libros/libro_lista.html', {'libros': libros})

def libro_detalle(request, pk):
    libros = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/libro_detalle.html', {'libros': libros})

def libro_nuevo(request):
    if request.method == "POST":
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            libro = form.save(commit=False)
            libro = Libro(
            #autor=form.cleaned_data['autor'],
            nombre=form.cleaned_data['nombre'],
            resumen=form.cleaned_data['resumen'],
            portadas=request.FILES)
            form.save()
        return redirect('libro_lista')
    else:
        form = LibroForm()
    return render(request, 'libros/libro_nuevo.html', {'form': form})

def libro_editar(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.save()
            return redirect('libro_detalle', pk=libro.pk)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/libro_editar.html', {'form': form})

def libro_eliminar(request, pk):
    libro = get_object_or_404(Libro,pk=pk)
    libro.delete()
    return redirect('libro_lista')

class BuscarView(TemplateView):

    def post(self, request, *args, **kwargs):
        buscar = request.POST['buscalo']
        libros = Libro.objects.filter(nombre__contains=buscar)
        if libros:
            datos = []
            for libro in libros:
                autores = libro.autor.all()
                datos.append(dict([(libro,autores)]))
            return render(request, 'libros/buscar.html', {'datos' :datos})
        else:
            autores = Autor.objects.filter(nombre__contains=buscar)
            return render(request, 'libros/buscar.html',
                        {'autores' :autores, 'autor' :True})


class BusquedaView(ListView):
    model = Autor
    template_name = 'libros/busqueda.html'
    context_objects_name = 'autores'
