from django.urls import path

from . import views

app_name = 'app1'
urlpatterns = [
    path('', views.show_map, name='index'),
]