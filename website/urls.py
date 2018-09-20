from django.urls import path

from website import views

urlpatterns = [
    path('', views.index, name="hlavní-stránka"),
    path('o-projektu/', views.about, name="o-projektu"),
    path('admin/', views.admin, name="přihlášení"),
    path('admin/logout', views.adminLogout, name="odhlášení"),
    path('admin/markers', views.markers, name="administrace"),
    path('admin/marker/<str:id>/edit', views.markerEdit, name="upravení-bodu"),
    path('admin/marker/<int:id>/info', views.markerInfo, name="informace-o-bodu"),
    path('admin/marker/<int:id>/delete', views.markerDelete, name="smazání-bodu"),
]
