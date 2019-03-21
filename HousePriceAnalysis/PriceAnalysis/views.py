from django.shortcuts import render
from PriceAnalysis import models
from mongoengine.queryset.visitor import Q
from django.shortcuts import HttpResponse
from django.http import JsonResponse
import pymongo
import json

from PriceAnalysis.GM_forecast import  * # 导入灰色预测模型


client = pymongo.MongoClient('mongodb+srv://averjing:Fu.ture1@housepriceanalysis-7vvvm.azure.mongodb.net/?retryWrites=true')
db = client["yearPriceData"]
col = db.get_collection("JS_suzhou")  # 找到该城市的集合名 放到showhouse中

def index(request):

    data = [
        {"name": "河北", "value": 8215}, {"name": "广东", "value": 12079}, {"name": "云南", "value": 7511},
        {"name": "广西", "value": 6164}, {"name": "吉林", "value": 5127}, {"name": "江苏", "value": 12018},
        {"name": "内蒙古", "value": 6273}, {"name": "辽宁", "value": 5763}, {"name": "安徽", "value": 7785},
        {"name": "湖北", "value": 6816}, {"name": "山西", "value": 5865}, {"name": "浙江", "value": 15167},
        {"name": "贵州", "value": 5650}, {"name": "福建", "value": 12952}, {"name": "山东", "value": 8293},
        {"name": "黑龙江", "value": 4443}, {"name": "河南", "value": 5717}, {"name": "陕西", "value": 6587},
        {"name": "新疆", "value": 4872}, {"name": "四川", "value": 7136}, {"name": "江西", "value": 7440},
        {"name": "甘肃", "value": 6319}, {"name": "湖南", "value": 5807}, {"name": "青海", "value": 7140},
        {"name": "西藏", "value": 10808}, {"name": "宁夏", "value": 4112},

        {"name": "重庆", "value": 11869}, {"name": "北京", "value": 60701}, {"name": "天津", "value": 21927},
        {"name": "上海", "value": 49569},
        {"name": "海南", "value": 7689},
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
            info_dic[area] = val[::-1] #逆序
        else:
            info_dic[area] = [0] * 12
    area_info = list(info_dic.keys())

    #print(area_info)
    #print(info_dic)
    context = {'areas': area_info, 'info_dict': info_dic, 'title': title}  # 上下文字典


    return JsonResponse(context)

def showForecast(request):

    # AJax 刷新数据 city value 是前端所选的地区和年份
    #  根据值从数据库中读取指定信息
    #  返回 某地区 某年 房价

    city = ''
    year = '2019' # 当前预测年份
    col2 = db.get_collection('Collections')

    if request.GET.get("city") is not None:
        city = request.GET.get("city")
    else:
        pass


    if city == '':
        city = 'JS_suzhou'
    else:
        name = city[:-1]

        city = col2.find_one({'city_name': name}, {'_id': 0, 'collection_name': 1})['collection_name']


    col = db.get_collection(city)  # 重新切换到新表

    title = str(year) + '房价走势预测图'
    area_info = col.find().distinct('area')  # 区域信息

    """空集合 传递给views 包含近年所有信息 "2019":[] "2018":[]"""

    info_dic = {}
    for area in area_info:
        price_data_last_year = col.find({"area": area, "year": "2018"}, {"_id": 0, "price": 1}) # last_year 要自己手动修改
        price_data_current_year = col.find({"area": area, "year": year}, {"_id": 0, "price": 1})
        price_last_year = [] #存放前一年的房价数据
        for i in price_data_last_year:
            price = int(i["price"][:-3])
            price_last_year.append(price)  # 取价格
        price_last_year.reverse() # 逆序 1-12月份
        price_current_year = [] #存放当前年份的房价数据
        for i in price_data_current_year:
            price = int(i.get("price")[:-3])
            price_current_year.append(price)
        price_current_year.reverse()
        for i in price_current_year:
            price_last_year.append(i)

        # price_last_year 是预测数列
        origin_data = price_last_year[:]  # 作平移处理时保留原始数据,两个数组互不影响，单纯的赋值是引用地址的传递
        if level_check(price_last_year):  # 判断原始数据是否符合级别校验
            print("符合级别校验,未做平移处理！")
            forecast_data = forecast(price_last_year, 0)
        else:
            print('不符合级别校验，作平移处理')
            data_handle(origin_data, 1)
            # 级别校验平移处理的平移值
            c = origin_data[0] - price_last_year[0]
            print('平移值c=', c)
            forecast_data = forecast(origin_data, c)
        if area == '1':  # 是1时取城市名
            area = col.find_one({'area': '1'}, {'_id': 0, 'city_name': 1})['city_name']
        for i in forecast_data:
            price_current_year.append(i)
        info_dic[area] = price_current_year

    area_info = list(info_dic.keys())

    #print(area_info)
    #print(info_dic)
    context = {'areas': area_info, 'info_dict': info_dic, 'title': title}  # 上下文字典


    return JsonResponse(context)
