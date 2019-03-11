"""定义新的URL模式"""

from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [

    # localhost:8001/???/
        #为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。
    path('', views.index, name='index'),
    path('show', views.showHouse, name='showHouse'),  # base :
    path('home', views.homePage, name='homePage'),
    path('show/<int:value>/', views.showHouse2, name='showHouse2'),  # base :
    path('historyPrice/', views.showHouse3, name='showHouse3'),
]