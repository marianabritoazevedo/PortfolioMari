from django.urls import include, path
from . import views

app_name = 'port'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('post/<slug>', views.details, name='details'),
]