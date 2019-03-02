from django.shortcuts import render

from .models import House
# Create your views here.

def index(request):

    return render(request, 'PriceAnalysis/base.html')

def homePage(request):

    return render(request, 'PriceAnalysis/home.html')

def showHouse(request):

    """显示房子信息 从model.House中"""

    houses = House.objects.all()
    context = {'house': houses}  # 上下文字典
    return render(request, 'PriceAnalysis/show.html', context)