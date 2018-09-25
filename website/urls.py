from django.urls import path

from website import views

urlpatterns = [
    path('', views.index, name="hlavní-stránka"),
    path('o-projektu/', views.about, name="o-projektu"),
    path('o-projektu2/', views.about2, name="o-projektu2"),
    path('admin/', views.admin, name="přihlášení"),
    path('admin/logout', views.admin_logout, name="odhlášení"),
    path('admin/markers', views.admin_marker_list, name="seznam-bodů"),
    path('admin/marker/<str:id>/edit', views.admin_marker_edit, name="úprava-a-vytvoření-bodu"),
    path('admin/marker/<int:id>/info', views.admin_marker_info, name="informace-o-bodu"),
    path('admin/marker/<int:id>/delete', views.admin_marker_delete, name="smazání-bodu"),
]
