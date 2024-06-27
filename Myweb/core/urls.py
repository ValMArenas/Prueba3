from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('productos/', views.productos, name="productos"),
    path('crear/', views.crear, name="crear"),
    path('detallePlanta/<id>/', views.detalle_planta, name="detallePlanta"),
    path('modificar/<id>/', views.modificar, name="modificar"),
    path('eliminar/<id>/', views.eliminar, name="eliminar"),
    path('logout/', views.cerrar, name="cerrar"),
    path('registrar/', views.registrar, name="registrar"),
    path('nosotras/', views.nosotras, name="nosotras"),
    path('contacto/', views.contacto, name="contacto"),
    path('sucursales/', views.sucursales, name="sucursales"),
    path('perfil/', views.detalle_user, name="perfil"),
    path('carrito/', views.carrito, name="carrito"),
]