from django.urls import include, path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('set_language/', views.set_language, name='set_language'),
]