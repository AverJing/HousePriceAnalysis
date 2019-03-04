from django.shortcuts import render

from echarts import models

# Create your views here.

def index(request):


    return render(request, 'PriceAnalysis/base.html')

    return render(request, 'PriceAnalysis/home.html')


def homePage(request):

    return render(request, 'PriceAnalysis/home.html')

def showHouse(request):

    """显示房子信息 从model.House中"""

    """显示房子信息 从model.House中"""

    # houses = models.House.objects[0:5]
    # print(houses)
    # context = {'house': houses}  # 上下文字典
    #return render(request, 'PriceAnalysis/show.html', context)
    return render(request, 'PriceAnalysis/show.html')