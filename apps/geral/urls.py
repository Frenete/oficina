from django.urls import path
app_name = 'geral'

from .import views
urlpatterns = [
    path('nova-oficina/', views.nova_oficina, name='nova_oficina'),
    path('oficinas/', views.lista_oficina, name='lista_oficina'),
    path('', views.home, name='home')
]