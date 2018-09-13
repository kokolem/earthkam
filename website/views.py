from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')


@login_required
def admin(request):
    return HttpResponse("Super. Jseš přihlášenej...")
