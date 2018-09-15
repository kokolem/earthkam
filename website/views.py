from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import MarkerForm


def index(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')


@login_required
def admin(request):
    if request.method == 'POST':
        form = MarkerForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = MarkerForm()

    return render(request, 'website/marker.html', {'form': form})
