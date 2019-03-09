from django.shortcuts import render
from PriceAnalysis import models
from mongoengine.queryset.visitor import Q
from django.shortcuts import HttpResponse
from django.http import JsonResponse
import pymongo
import json

client = pymongo.MongoClient('localhost', 27017)
db = client["import"]
col = db.get_collection("JS_suzhou")  # 找到该城市的集合名 放到showhouse中
# Create your views here.

def index(request):


    #return render(request, 'PriceAnalysis/base.html')

    return render(request, 'PriceAnalysis/home.html')


def homePage(request):

    return render(request, 'PriceAnalysis/home.html')

def showHouse(request):

    """显示房子信息 从model.House中"""
    #从数据库读区域



    info = col.find({"city_name": '苏州'})
    title = '2018'
    area_info = col.find().distinct('area')  # 区域信息
        #years_info = col.find().distinct('year')  # 年份信息
    xaxis = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']

        # 地区 吴中 年份 从year_info 中读取
    info_dic = {} # 空集合 传递给views 包含近年所有信息 "2019":[] "2018":[]
    for area in area_info:

        price_data = col.find({"area": area, "year": "2018"}, {"_id": 0, "price": 1})
        val = []
        for i in price_data:
            val.append(i["price"][:-3]) # 取价格
            #print(i["price"][:-3])
        if area == '1':
            area = '苏州'
        info_dic[area] = val
    area_info = list(info_dic.keys())
    #print(area_info)


    context = {'PriceHistory': info, 'areas': area_info, 'xaxis': xaxis, 'info_dict': info_dic, 'title': title}  # 上下文字典
    return render(request, 'PriceAnalysis/show.html', context)

def showHouse2(request, value=0):
    #print(value)
    return render(request, 'PriceAnalysis/show.html', {"value": value})
def showHouse3(request):
    city = ''
    value = '2018'

    city_dict = {
        "苏州市": "JS_suhzou",
        "徐州市": "JS_xuhzou",
        "盐城市": "JS_yancheng",
        "无锡市": "JS_wuxi",
        "泰州市": "JS_taizhou",
        "扬州市": "JS_yangzhou",
        "镇江市": "JS_zhenjiang",
        "淮安市": "JS_huaian",
        "连云港市": "JS_lianyungang",
        "南京市": "JS_nanjing",
        "南通市": "JS_nantong",
        "沭阳市": "JS_shuyang",
        "宿迁市": "JS_suqian",
        "昆山市": "JS_ks",


    }
    if request.GET.get("city") is not None:
        city = request.GET.get("city")
        #print('传入的城市名' + city)
    else:
        pass
        #print('没有得到city')

    if request.GET.get("value") is not None:
        value = request.GET.get("value")
        #print('传入的年份' + value)
    else:
        pass
        #print('没有得到年份')

    if city == '' or city == '苏州市':
        city = 'JS_suzhou'
    else:
        city = city_dict[city]


    #print(value, city)
    col = db.get_collection(city)
    title = str(value) +'房价走势图'
    #print(title)
    area_info = col.find().distinct('area')  # 区域信息

    xaxis = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']

    # 地区 吴中 年份 从year_info 中读取
    info_dic = {}  # 空集合 传递给views 包含近年所有信息 "2019":[] "2018":[]
    for area in area_info:

        price_data = col.find({"area": area, "year": value}, {"_id": 0, "price": 1})
        val = []
        for i in price_data:
            val.append(i["price"][:-3])  # 取价格
            # print(i["price"][:-3])
        if area == '1':
            area = col.find_one({'area':'1'}, {'_id': 0, 'city_name': 1})['city_name']
            #print('area: ', area)
        info_dic[area] = val
    area_info = list(info_dic.keys())
    #print(area_info)
    #print(info_dic)
    context = {'areas': area_info, 'xaxis': xaxis, 'info_dict': info_dic, 'title': title}  # 上下文字典


    return JsonResponse(context) #, content_type='application/json'

def found_area(cityname=''):
    """根据城市找到城市中所有区"""
    pass