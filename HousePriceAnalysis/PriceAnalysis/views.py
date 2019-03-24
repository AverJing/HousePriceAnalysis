from django.shortcuts import render
from PriceAnalysis import models
from mongoengine.queryset.visitor import Q
from django.shortcuts import HttpResponse
from django.http import JsonResponse
import pymongo
import json

client = pymongo.MongoClient('mongodb+srv://averjing:Fu.ture1@housepriceanalysis-7vvvm.azure.mongodb.net/?retryWrites=true')
db2 = client["lianjia"]
db = client["yearPriceData"]
# 找到该城市的集合名 放到showhouse中
# Create your views here.

def index(request):
    #return render(request, 'PriceAnalysis/base.html')
    #return render(request, 'PriceAnalysis/home.html')
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
        {"name": "海南", "value": 7689}
    ]
    json_data = {
        'data': json.dumps(data)
    }
    return render(request, 'PriceAnalysis/home.html', json_data)

def homePage(request):

    return render(request, 'PriceAnalysis/home.html')

def getCityPinyin(city):
    col2 = db2.get_collection('collection')  #
    query = col2.find_one({'city': city }, {'_id': 0, 'name': 1, 'area': 1})
    return query

def showHouse(request, city='苏州'):
    """显示房子信息 从model.House中"""
    #从数据库读区域

    # info = col.find({"city_name": '苏州'})
    # #info = col.find({"city_name": '苏州'})
    # title = '2018'
    # area_info = col.find().distinct('area')  # 区域信息
# def showHouse(request, province=' ', city=' '):
#     #不能是'' 反向解析时会出现错误
#     """显示房子信息 从前端获取province 和 city 参数
#     只有procince时 是请求历史房价 只有city时 查询当前二手房信息
#     先根据省份找到省中所有市 展示出来 默认 江苏 苏州
#     查城市时根据城市名在collections中获取城市表名，根据表名获取城市中各个区"""

    #从数据库读区域

    #if province == ' ':   #只传城市 默认从数据库中搜索该城市的10条信息

    query = getCityPinyin(city)
    city_table = query["name"]+"_ershoufang"

    # 获取城市对应表明 suzhou_ershoufang
    area_info = query["area"]
    #print(area_info)

    col = db2.get_collection(city_table)  # 重新切换到新表
    data = col.find({}).limit(10)
    data_list = []  # 空集合 传递给views 包含前10条信息

    for item in data:
        data_list.append([item['title'], item['area'], int(item['price']), item['communityName'], item['房屋户型'], item['建筑面积'], item['户型结构'], item['装修情况'], item['所在楼层']])

    context = {'city': city, 'areas': area_info, 'houseData': data_list, 'count': len(data_list)}
    return render(request, 'PriceAnalysis/data_analysis.html', context)

def showHistory(request, city="苏州"):
# if city == ' ':  # 只传省份
    col2 = db.get_collection("Collections")  # 查询省中城市
    city_info = col2.find_one({'city_name': city})

    col = db.get_collection(city_info["collection_name"])
    title = '2018'
    area_info = col.find().distinct('area')  # 区域信息

    info_dic = {} # 空集合 传递给views 包含近年所有信息 "2019":[] "2018":[]
    for area in area_info:

        price_data = col.find({"area": area, "year": "2018"}, {"_id": 0, "price": 1})
        val = []
        for i in price_data:
            val.append(int(i["price"][:-3]))   # 取价格
        if area == '1':
            area = city
        info_dic[area] = val[::-1]
    area_info = list(info_dic.keys())

    #print(info_dic)
    
    context = {'areas': area_info, 'info_dict': info_dic, 'title': title}  # 上下文字典 城市 地区 房价 标签
    return render(request, 'PriceAnalysis/show.html', context)


def showHouse3(request):

    # AJax 刷新数据 city value 是前端所选的地区和年份
    #  根据值从数据库中读取指定信息
    #  返回 某地区 某年 房价
    db = client["yearPriceData"]
    city = ''
    year = '2019'
    col2 = db.get_collection('Collections')

    if request.GET.get("district") is not None:
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
    print(context)
    return JsonResponse(context)

def queryHouse(request):
    city = request.GET.get("city")
    print(city)
    name = request.GET.get("district") or '吴中.'
    price = request.GET.get("price") or '0-1000000'
    house_type = request.GET.get("type")
    area = request.GET.get("area") or '0-10000'

    # name 后面多了一个" " ??? 很迷

    #print(name)
    print(price)
    print(len(price))

    price_list = price.split('-')
    area_list = area.split('-')

    db2 = client["lianjia"]
    col2 = db2.get_collection('collection')  #
    query = col2.find_one({'city': city }, {'_id': 0, 'name': 1, 'area': 1})

    col = db2.get_collection(query['name']+"_ershoufang")  # 切换表
    data = col.find(
        {'area': name[:-1],
         '房屋户型': {'$regex': house_type},
         'price': {'$gt': int(price_list[0]), '$lt': int(price_list[1])},
         '建筑面积': {'$gt': int(area_list[0]), '$lt': int(area_list[1])}}
    ).limit(10)  #
    data_list = []  # 空集合 传递给views 包含前10条信息

    for item in data:

        data_list.append(
            [item['title'], item['area'], int(item['price']), item['communityName'], item['房屋户型'], item['建筑面积'],
             item['房屋朝向'], item['装修情况'], item['所在楼层']])

    context = {'houseData': data_list, 'count': len(data_list)}

    return JsonResponse(context)