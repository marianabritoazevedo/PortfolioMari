from django.urls import include, path
from . import views

app_name = 'port'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('search-certificado/', views.search_certificado, name='search_certificado'),
    path('post/<slug>', views.details, name='details'),
    path('certificados/', views.certificado, name='certificado'),
    path('certificados/<slug>', views.certificado_details, name='certificado_details'),
]