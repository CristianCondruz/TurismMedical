from django.urls import path, reverse_lazy, re_path, include
from django.contrib.auth import views as auth_views
from .views import ListaAfectiuniView, adaugare_afectiuni_view, detalii_afectiune, cazare_view, ListaProceduriView


app_name = 'afectiuni'

urlpatterns = [
    path('adaugare_afectiuni', adaugare_afectiuni_view,name='adaugare_afectiuni'),
    path('listare_afectiuni', ListaAfectiuniView.as_view(), name='listare_afectiuni'),
    re_path('afectiune/(?P<pk>\d+)', detalii_afectiune, name='afectiuni_detail'),
    re_path('cazare/(?P<pk>\d+)',cazare_view, name='cazare_detail'),
    path('listare_proceduri', ListaProceduriView.as_view(), name='listare_proceduri'),
]
