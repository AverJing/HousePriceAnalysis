"""HousePriceAnalysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
import PriceAnalysis.views as pv
from django.conf.urls import include,url

from django.urls import path, include
from login import views as loginV
from echarts import views as chartV
from main import views as mainV
import PriceAnalysis.views as pv
import waterflow.views as waterflowV

urlpatterns = [
    path('', mainV.index),
    path('select/', mainV.selectCity, name="selectCity"),
    path('', include(('PriceAnalysis.urls', 'PriceAnalysis'), namespace='PriceAnalysis')),  # , namespace='lea
    #path('index/', pv.index),
    # path('', pv.index, name='index'),
    # path('show', pv.showHouse, name='showHouse'),  # base :
    # path('home', pv.homePage, name='homePage'),
    #path('main/', mainV.main_html),
    path('newlogin',mainV.new_login, name="newlogin"),#转到新的ajax登录页面
    path('ajaxregister/',mainV.new_register),#转到新的ajax注册页面
    path('ajaxlogin',mainV.login),
    path('reg',mainV.ajaxregister),
    path('logout/', mainV.logout),
    #path('index/',mainV.indexAddEcharts),
    path('excellentHouse/',waterflowV.excellent_house),
    #path('admin/', admin.site.urls),
    

    #path('index/', loginV.index),
    path('login/', loginV.login), 
    path('register/', loginV.register),
    path('captcha/', include('captcha.urls')),
    path('map/', chartV.echart),
    #path('echarts/index/', chartV.index),
    #path('echarts/map/', chartV.getAll),
    path('echarts/baidumap/<str:locations>',chartV.baiduMap, name="baidumap"),
    path('echarts/baidumap/<str:locations>/<str:base>',chartV.baiduMap, name="baidumap"),
    path('admin/', admin.site.urls),
    path('<str:location>/', mainV.index, name="index"), 
    #path('', pv.showHouse, name='showHouse', namespace='PriceAnalysis'), 
]
