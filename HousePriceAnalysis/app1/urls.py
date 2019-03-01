from django.urls import path

from . import views

app_name = 'app1'
urlpatterns = [
    path('<str:china>/', views.china_map, name='index'),
    path('<str:china>/<str:province>/', views.province_map, name='index'),
    path('<str:china>/<str:province>/<str:city>', views.city_map, name='index'),
]