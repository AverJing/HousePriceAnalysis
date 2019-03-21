from django.shortcuts import render
from PriceAnalysis import models
from mongoengine.queryset.visitor import Q
from django.shortcuts import HttpResponse
from django.http import JsonResponse
import pymongo
import json

client = pymongo.MongoClient('mongodb+srv://averjing:Fu.ture1@housepriceanalysis-7vvvm.azure.mongodb.net/?retryWrites=true')
db = client["yearPriceData"]
 # 找到该城市的集合名 放到showhouse中
# Create your views here.

def index(request):


    return render(request, 'PriceAnalysis/home.html')

def homePage(request):

    return render(request, 'PriceAnalysis/home.html')

def showHouse(request, province=' ', city=' '):
    #不能是'' 反向解析时会出现错误
    """显示房子信息 从前端获取province 和 city 参数
    只有procince时 是请求历史房价 只有city时 查询当前二手房信息
    先根据省份找到省中所有市 展示出来 默认 江苏 苏州
    查城市时根据城市名在collections中获取城市表名，根据表名获取城市中各个区"""

    #从数据库读区域

    if province == ' ':   #只传城市 默认从数据库中搜索该城市的10条信息

        name = city
        col2 = db.get_collection('Collections')  #
        city = col2.find_one({'city_name': city}, {'_id': 0, 'collection_name': 1})['collection_name']
        # print(city)
        col = db.get_collection(city)  # 重新切换到新表
        #print(name)
        area_info = col.find().distinct('area')  # 区域信息 包含1 不要
        del area_info[0]  # 不要1

        db2 = client["lianjia"]
        col = db2.get_collection('suzhou_ershoufang')  # 切换表
        data = col.find({}).limit(10)
        data_list = []  # 空集合 传递给views 包含前10条信息

        for item in data:
            #print(item)
            data_list.append([item['title'], item['area'], int(item['price']), item['communityName'], item['房屋户型'], item['建筑面积'], item['户型结构'], item['装修情况'], item['所在楼层']])
        #print(data_list[0][0])
        context = {'city': name, 'areas': area_info, 'houseData': data_list, 'count': len(data_list)}
        return render(request, 'PriceAnalysis/data_analysis.html', context)
    if city == ' ':  # 只传省份
        col = db.get_collection("JS_suzhou")
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
    #print(city+'sss')
    if city == '':
        city = 'JS_suzhou'
    else:
        name = city[:-1]  # 去空格

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
            info_dic[area] = val[::-1]  # 逆序
        else:
            info_dic[area] = [0] * 12
    area_info = list(info_dic.keys())


    #print(info_dic)
    context = {'areas': area_info, 'info_dict': info_dic, 'title': title}  # 上下文字典


    return JsonResponse(context)

def queryHouse(request):
    print('sss')
    name = request.GET.get("city")
    # 获取区
    # col2 = db.get_collection('collections')  #
    # city = col2.find_one({'city_name': '苏州'}, {'_id': 0, 'collection_name': 1})['collection_name']
    # col = db.get_collection(city)  # 重新切换到新表
    # area_info = col.find().distinct('area')  # 区域信息 包含1 不要
    # del area_info[0]  # 不要1

    db2 = client["lianjia"]
    col = db2.get_collection('suzhou_ershoufang')  # 切换表
    data = col.find({'area': "吴中"}).limit(10)
    data_list = []  # 空集合 传递给views 包含前10条信息

    for item in data:
        #print(item)
        data_list.append(
            [item['title'], item['area'], int(item['price']), item['communityName'], item['房屋户型'], item['建筑面积'],
             item['户型结构'], item['装修情况'], item['所在楼层']])
    print(data_list[0][0])
    context = {'city': '苏州', 'houseData': data_list, 'count': len(data_list)}
    #return render(request, 'PriceAnalysis/data_analysis.html', context)
    return JsonResponse(context)