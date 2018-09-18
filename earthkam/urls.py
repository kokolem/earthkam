"""earthkam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include

from website import views

urlpatterns = [
    path('', views.index, name="index"),
    path('o-projektu/', views.about, name="o-projektu"),
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', views.admin, name="přihlášení"),
    path('admin/markers', views.markers, name="administrace"),
    path('admin/marker/<str:id>/edit', views.markerEdit, name="upravení-bodu"),
    path('admin/marker/<int:id>/info', views.markerInfo, name="informace-o-bodu"),
    path('admin/marker/<int:id>/delete', views.markerDelete, name="smazání-bodu"),
]
