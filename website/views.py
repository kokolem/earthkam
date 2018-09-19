from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MarkerForm
from .models import Marker


def index(request):
    # Hlavní stránka

    map_markers = Marker.objects.all()
    return render(request, 'website/index.html', {"markers": map_markers})


def about(request):
    # Stránka o projektu
    markers_count = len(Marker.objects.all())
    return render(request, 'website/about.html', {"markers_count": markers_count})


@login_required
def markers(request):
    # Hlavní admin stránka - vypsané body

    map_markers = Marker.objects.all()
    return render(request, 'website/markers.html', {"markers": map_markers})


@login_required
def markerEdit(request, id):
    # Formulář ná úpravu / vytvoření bodu

    if id == "new":
        if request.method == 'POST':
            form = MarkerForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/admin')
        else:
            form = MarkerForm()
    else:
        instance = Marker.objects.get(pk=int(id))

        if request.method == 'POST':
            form = MarkerForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/admin')

        else:
            form = MarkerForm(instance=instance)

    return render(request, 'website/markerEdit.html', {'form': form, 'id': id})


@login_required
def markerInfo(request, id):
    # Veškeré informace o bodu

    map_marker = Marker.objects.get(pk=id)
    return render(request, 'website/markerInfo.html', {'marker': map_marker})


@login_required
def markerDelete(request, id):
    # Smazání bodu

    Marker.objects.get(pk=id).delete()
    return HttpResponseRedirect('/admin')


@login_required
def admin(request):
    # Stránka na přihlašování

    return HttpResponseRedirect('/admin/markers')
