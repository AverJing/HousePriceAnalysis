from django.shortcuts import render

from echarts import models
# Create your views here.
from django.http import JsonResponse
def index(request):
    return render(request, 'PriceAnalysis/home.html')

import  pymongo
import json


def test(request):
    return render(request,'PriceAnalysis/test.html')
def show_ajax(request):
    #value = 2019
    value = request.POST.get('value')
    client = pymongo.MongoClient('localhost', 27017)
    db = client["HousePriceHistory"]
    col = db.get_collection("JS_suzhou") # 找到该城市的集合名
    areas = col.find({"year":str(value),"month":"03"},{"_id":0,"area":1}) # 查找该城市的所有区域
    ares = [] # 存放区域的名字
    datalist = [] # 存放该区域相应年份的数据
    for i in areas:
        area = i.get("area") # 获取area的值
        ares.append(area) # 添加到list中
    for i in range(len(ares)): # 遍历每个区域，查找对应区域的房价数据
        #print(ares[i]) # 打印区域名

        data = col.find({"area": ares[i], "year": str(value)}, {"price": 1, "_id": 0})
        res = [] # 存放每个区域的房价数据

        for i in data: # 去掉元，只取数字
            price = i.get("price")
            end = price.index("元")
            price = price[:end]
            res.append(int(price)) # 房价信息时int类型，12月份-1月份
        res.reverse() #调整数据顺序，1月份-12月份

        datalist.append(res) # list嵌套list，将每一个区域的数据list当做一个元素

    ares[0] = "苏州" # 调整area 1 为城市名

    dictionary  = dict(zip(ares,datalist)) # 将两个list合成一个dict，将区域名与对应的数据对应起来，分别作key和value
    #return JsonResponse({'areas':json.dumps(ares),'datalist':json.dumps(dictionary)})
    #return render(request, 'PriceAnalysis/show.html',{'areas':json.dumps(ares),'datalist':json.dumps(dictionary)})
def showHouse(request,value=2019):
    client = pymongo.MongoClient('localhost', 27017)
    db = client["HousePriceHistory"]
    col = db.get_collection("JS_suzhou") # 找到该城市的集合名
    areas = col.find({"year":str(value),"month":"03"},{"_id":0,"area":1}) # 查找该城市的所有区域
    ares = [] # 存放区域的名字
    datalist = [] # 存放该区域相应年份的数据
    for i in areas:
        area = i.get("area") # 获取area的值
        ares.append(area) # 添加到list中
    for i in range(len(ares)): # 遍历每个区域，查找对应区域的房价数据
        #print(ares[i]) # 打印区域名
        data = col.find({"area": ares[i], "year": str(value)}, {"price": 1, "_id": 0})
        res = [] # 存放每个区域的房价数据
        for i in data: # 去掉元，只取数字
            price = i.get("price")
            end = price.index("元")
            price = price[:end]
            res.append(int(price)) # 房价信息时int类型，12月份-1月份
        res.reverse() #调整数据顺序，1月份-12月份
        #for i in res:# 测试打印
            #print(type(i), i)
        datalist.append(res) # list嵌套list，将每一个区域的数据list当做一个元素
    #for i in datalist: # 测试打印
        #print(i)
    ares[0] = "苏州" # 调整area 1 为城市名
    #for a in ares:
        #print(a)
    dictionary  = dict(zip(ares,datalist)) # 将两个list合成一个dict，将区域名与对应的数据对应起来，分别作key和value
    #dictionary.items()
    #print(dictionary) #测试打印
    #print(dictionary.items())
    #print(json.dumps(ares))
    return render(request, 'PriceAnalysis/show.html',{'areas':json.dumps(ares),'datalist':json.dumps(dictionary)})

#homePage() #做测试

def homePage(request):

    """显示房子信息 从model.House中"""
    houses = models.House.objects[0:5]
    print(houses)
    context = {'house': houses}  # 上下文字典
    return render(request, 'PriceAnalysis/home.html', context)

#def Province(request,province='江苏'):
 #   return render(request,'PriceAnalysis/show.html')