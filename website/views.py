from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import MarkerForm
from .models import Marker


def index(request):
    # Hlavní stránka

    map_markers = Marker.objects.all()
    return render(request, 'website/index.html', {"markers": map_markers})


def about(request):
    # Stránka o projektu

    return render(request, 'website/about.html')


@login_required
def markers(request):
    # Hlavní admin stránka - vypsané body

    map_markers = Marker.objects.all()
    return render(request, 'website/markers.html', {"markers": map_markers})


@login_required
def marker(request, id):
    # Formulář ná úpravu / vytvoření bodu

    if id == "new":
        if request.method == 'POST':
            form = MarkerForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('Nový bod byl vytvořen.')
        else:
            form = MarkerForm()
    else:
        instance = Marker.objects.get(pk=int(id))

        if request.method == 'POST':
            form = MarkerForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponse('Bod byl upraven.')

        else:
            form = MarkerForm(instance=instance)

    return render(request, 'website/marker.html', {'form': form, 'id': id})


@login_required
def admin(request):
    # Stránka na přihlašování

    return HttpResponseRedirect('/admin/markers')
