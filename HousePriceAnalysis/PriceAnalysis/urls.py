"""定义新的URL模式"""

from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [

    # localhost:8001/???/
        #为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。
    #path('', views.index, name='index'),
    path('show/<str:city>', views.showHouse, name='showHouse'),  # base :
    path('showHistory/<str:city>', views.showHistory, name="showHistory"),
    #path('show/<str:province>/<str:city>/', views.showHouse, name='showHouse'),  # base :
    path('home', views.homePage, name='homePage'),
    path('historyPrice/', views.showHouse3, name='showHouse3'),
    path('queryHouse/', views.queryHouse, name='queryHouse'),
]