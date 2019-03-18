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

def baiduMap(request):
    # 查询所有的数据
    #inform = models.House.objects.to_json()
    if not request.session.get('is_login', None):
        return redirect('/index/')
    else:
        request.session['map'] = True
        inform = models.House.objects
        print(inform)
        #统计区域及各区均价
        area = []
        avg_prices = []
        count = []
        houses = []
        for item in inform:  #统计区域及区域总价
            dict = {
                'area': item.district_main,
                'name': item.name,
                'price': item.main_price,
                'longitude': item.lng,
                'latitude': item.lat
            }
            houses.append(dict)
            p = item.main_price
            if item.district_main not in area:
                area.append(item.district_main)
                if (p != '暂无'):
                    avg_prices.append(int(p))
                    count.append(1)
                else:
                    avg_prices.append(0)
                    count.append(0)
            else:
                if (p != '暂无'):
                    currIndex = area.index(item.district_main)
                    avg_prices[currIndex] += int(p)
                    count[currIndex] += 1

        for index in range(len(avg_prices)):  #将总价转为万为单位的均价
            if count[index] != 0:
                avg_prices[index] /= count[index]
                avg_prices[index] /= 10000
                avg_prices[index] = round(avg_prices[index], 2)#小数点后保留两位



        json_data = {
            'area': json.dumps(area),
            'prices': json.dumps(avg_prices),
            'houses': json.dumps(houses)
        }
        return render(request, "echarts/baidumap.html", json_data)