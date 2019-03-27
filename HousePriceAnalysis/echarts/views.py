from django.shortcuts import render,redirect
import math
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from echarts import models
from urllib.request import urlopen, quote
import json
import pymongo

client = pymongo.MongoClient('mongodb+srv://averjing:Fu.ture1@housepriceanalysis-7vvvm.azure.mongodb.net/?retryWrites=true')
db = client["lianjia"]

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
    if not request.session.get('islogin', None):
        return redirect('/index/')
    else:
        request.session['map'] = True
        inform = models.House.objects.to_json()
        return render(request,"echarts/map.html",{'inform':inform})

# def baiduMap(request, locations="南京"):
#     # 查询所有的数据
#     #inform = models.House.objects.to_json()
#     if not request.session.get('islogin', None):
#         return redirect('/index/')
#     else:
#         table_name = db.get_collection("collection").find_one({'city':locations})
#         request.session['map'] = True
#         inform = db.get_collection(table_name['name']).find()
#         print(inform)
#         #统计区域及各区均价
#         area = []
#         avg_prices = []
#         count = []
#         houses = []
#         for item in inform:  #统计区域及区域总价
#             dict = {
#                 'area': item["district_main"],
#                 'name': item["name"],
#                 'price': item["main_price"],
#                 'longitude': item["lng"],
#                 'latitude': item["lat"]
#             }
#             houses.append(dict)
#             p = item["main_price"]
#             if item["district_main"] not in area:
#                 area.append(item["district_main"])
#                 if (p != '暂无'):
#                     avg_prices.append(int(p))
#                     count.append(1)
#                 else:
#                     avg_prices.append(0)
#                     count.append(0)
#             else:
#                 if (p != '暂无'):
#                     currIndex = area.index(item["district_main"])                  
#                     avg_prices[currIndex] += int(p)
#                     count[currIndex] += 1

#         for index in range(len(avg_prices)):  #将总价转为万为单位的均价
#             if count[index] != 0:
#                 avg_prices[index] /= count[index]
#                 avg_prices[index] /= 10000
#                 avg_prices[index] = round(avg_prices[index], 2)#小数点后保留两位

#         json_data = {
#             'area': json.dumps(area),
#             'prices': json.dumps(avg_prices),
#             'houses': json.dumps(houses),
#             'locations' : json.dumps(locations)
#         }
#         print(avg_prices)
#         return render(request, "echarts/baidumap2.html", json_data)
def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'gnOslEM7knsFAmaGTEnM2Axs0jy5Vi0F'
    add = quote(address) #由于本文城市变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode() #将其他编码的字符串解码成unicode
    temp = json.loads(res) #对json数据进行解析
    return temp 

def baiduMap(request, locations="南京"):
    # 查询所有的数据
    # inform = models.House.objects.to_json()
    if not request.session.get('islogin', None):
        return redirect('/')
    else:
        print(locations)
        request.session['map'] = True
        table_name = db.get_collection("collection").find_one({'city':locations})
        inform = db.get_collection(table_name['name']).find()
        print(inform)
        city_lat_lag = getlnglat(locations)
        # 统计区域及各区均价
        area = []
        houses = []
        for item in inform:  # 统计区域及区域总价
            if item["lng"] == '暂无':
                continue
            if abs(item["lng"]  - city_lat_lag['result']['location']['lng']) < 1.0 and abs(item["lat"]  - city_lat_lag['result']['location']['lat']) < 1.0:
                house_dict = {
                    'area': item["district_main"],
                    'name': item["name"],
                    'price': item["main_price"],
                    'longitude': item["lng"],
                    'latitude': item["lat"]
                }
                houses.append(house_dict)
                if item["district_main"] not in area:
                    area.append(item["district_main"])

        center = city_lat_lag['result']['location']

        json_data = {
            'center': json.dumps(center),
            'area': json.dumps(area),
            'houses': json.dumps(houses),
            'location':locations
        }
        return render(request, "echarts/baidumap.html", json_data)