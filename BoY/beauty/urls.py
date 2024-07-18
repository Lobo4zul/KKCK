from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('tyc/', views.terminos, name="terminos"),
    path('privacidad_y_politicas/', views.privacidadpoliticas, name="privacidadpoliticas"),
    path('blog/', views.blog, name="blog"),
    path('actitud/', views.actitud, name='actitud'),
    path('cabello-afro/', views.cabello_afro, name='cabello_afro'),
    path('cuidado-cabello/', views.cuidado_cabello, name='cuidado_cabello'),
    path('oficina/', views.oficina, name='oficina'),
    path('primavera-verano/', views.primavera_verano, name='primavera_verano'),
    path('skincare/', views.skincare, name='skincare'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('resena/', views.resena, name='resena'),
    path('pielesOscuras', views.pielesOscuras, name='pielesOscuras'),
    path('pielesMedias', views.pielesMedias, name='pielesMedias'),
    path('pielesClaras', views.pielesClaras, name='pielesClaras'),
]