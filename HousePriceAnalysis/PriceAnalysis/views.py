from django.shortcuts import render
from PriceAnalysis import models
from mongoengine.queryset.visitor import Q
from django.shortcuts import HttpResponse
from django.http import JsonResponse
import pymongo
import json

client = pymongo.MongoClient('mongodb+srv://averjing:Fu.ture1@housepriceanalysis-7vvvm.azure.mongodb.net/?retryWrites=true')
db = client["yearPriceData"]
col = db.get_collection("JS_suzhou")  # 找到该城市的集合名 放到showhouse中
# Create your views here.

def index(request):


    #return render(request, 'PriceAnalysis/base.html')
    #return render(request, 'PriceAnalysis/home.html')
    data = [
        {"name": "新疆", "value": 20}, {"name": "西藏", "value": 100},
        {"name": "青海", "value": 100}, {"name": "甘肃", "value": 100},
        {"name": "四川", "value": 100}, {"name": "云南", "value": 100},
        {"name": "内蒙古", "value": 100}, {"name": "宁夏", "value": 100},
        {"name": "陕西", "value": 170}, {"name": "重庆", "value": 100},
        {"name": "贵州", "value": 170}, {"name": "广西", "value": 100},
        {"name": "山西", "value": 10}, {"name": "河南", "value": 100},
        {"name": "湖北", "value": 100}, {"name": "湖南", "value": 100},
        {"name": "广东", "value": 100}, {"name": "河北", "value": 120},
        {"name": "北京", "value": 100}, {"name": "天津", "value": 100},
        {"name": "山东", "value": 100}, {"name": "安徽", "value": 100},
        {"name": "江西", "value": 100}, {"name": "江苏", "value": 100},
        {"name": "浙江", "value": 100}, {"name": "上海", "value": 140},
        {"name": "福建", "value": 17}, {"name": "海南", "value": 100},
        {"name": "黑龙江", "value": 45}, {"name": "吉林", "value": 100},
        {"name": "辽宁", "value": 100}
    ]
    json_data = {
        'data': json.dumps(data)
    }
    return render(request, 'PriceAnalysis/home.html', json_data)


def homePage(request):

    return render(request, 'PriceAnalysis/home.html')

def showHouse(request, province='江苏'):

    """显示房子信息 从model.House中"""
    #从数据库读区域

    info = col.find({"city_name": '苏州'})
    #info = col.find({"city_name": '苏州'})
    title = '2018'
    area_info = col.find().distinct('area')  # 区域信息

    info_dic = {} # 空集合 传递给views 包含近年所有信息 "2019":[] "2018":[]
    for area in area_info:

        price_data = col.find({"area": area, "year": "2018"}, {"_id": 0, "price": 1})
        val = []
        for i in price_data:
            val.append(int(i["price"][:-3]))   # 取价格
        if area == '1':
            area = '苏州'
        info_dic[area] = val[::-1]
    area_info = list(info_dic.keys())

    #print(info_dic)
    col2 = db.get_collection("Collections")  # 查询省中城市

    city_info = col2.find({'province': province}).distinct('city_name')

    context = {'pro': province, 'cities': city_info, 'areas': area_info, 'info_dict': info_dic, 'title': title}  # 上下文字典 城市 地区 房价 标签
    return render(request, 'PriceAnalysis/show.html', context)


def showHouse3(request):

    # AJax 刷新数据 city value 是前端所选的地区和年份
    #  根据值从数据库中读取指定信息
    #  返回 某地区 某年 房价

    city = ''
    year = '2019'
    col2 = db.get_collection('Collections')

    if request.GET.get("city") is not None:
        city = request.GET.get("city")
    else:
        pass

    if request.GET.get("year") is not None:
        year = request.GET.get("year")
    else:
        pass

    if city == '':
        city = 'JS_suzhou'
    else:
        name = city[:-1]

        city = col2.find_one({'city_name': name}, {'_id': 0, 'collection_name': 1})['collection_name']


    col = db.get_collection(city)  # 重新切换到新表
    title = str(year) + '房价走势图'
    area_info = col.find().distinct('area')  # 区域信息

    """空集合 传递给views 包含近年所有信息 "2019":[] "2018":[]"""

    info_dic = {}
    for area in area_info:
        price_data = col.find({"area": area, "year": year}, {"_id": 0, "price": 1})

        val = []
        for i in price_data:
            price = int(i["price"][:-3])
            val.append(price)  # 取价格

        if area == '1':  # 是1时取城市名
            area = col.find_one({'area': '1'}, {'_id': 0, 'city_name': 1})['city_name']
        # 过滤不合格的数据
        if len(val) == 3 or len(val) == 12:
            info_dic[area] = val[::-1]
        else:
            info_dic[area] = [0] * 12
    area_info = list(info_dic.keys())

    #print(area_info)
    #print(info_dic)
    context = {'areas': area_info, 'info_dict': info_dic, 'title': title}  # 上下文字典


    return JsonResponse(context)

def found_area(cityname=''):
    """根据城市找到城市中所有区"""
    pass