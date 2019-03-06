from django.shortcuts import render

from echarts import models
import json
# Create your views here.

def index(request):
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

def showHouse(request):

    """显示房子信息 从model.House中"""

    houses = models.House.objects[0:5]
    print(houses)
    context = {'house': houses}  # 上下文字典
    return render(request, 'PriceAnalysis/show.html', context)