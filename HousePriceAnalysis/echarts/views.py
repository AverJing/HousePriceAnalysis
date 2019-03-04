from django.shortcuts import render,redirect
import math
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from echarts import models
import json

# Create your views here.
def echart(request):
    return render(request, 'echarts/echarts.html')

def index(request):
    return render(request,"echarts/index.html")

def getAllByPage(request):
    # 限制每一页显示的条目数量
    limit = 10
    # 查询所有的数据
    inform = models.House.objects
    paginator = Paginator(inform,limit)
    # 从url中获取页码参数
    page_num = request.GET.get('page',1)
    loaded = paginator.page(page_num)
    context = {
        'inform':loaded
    }
    return render(request,"echarts/index.html",context)

def getAll(request):
    # 查询所有的数据
    #inform = models.House.objects.to_json()
    if not request.session.get('is_login', None):
        return redirect('/index/')
    else:
        request.session['map'] = True
        inform = models.House.objects.to_json()
        return render(request,"echarts/map.html",{'inform':inform})
