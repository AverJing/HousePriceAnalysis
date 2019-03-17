from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def excellent_house(request):
    sqlJson = [
        {'title': '息州豪府', 'intro': '爆料，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
                'src': 'images/1.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '锦绣玉成', 'intro': '爆料了，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
                'src': 'images/2.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '月亮湾', 'intro': '爆料了，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
                'src': 'images/3.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '息州豪府', 'intro': '爆料了，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
                'src': 'images/4.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '息州豪府', 'intro': '爆料，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
         'src': 'images/3.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '息州豪府', 'intro': '爆料了，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
         'src': 'images/2.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '息州豪府', 'intro': '爆料了，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
         'src': 'images/1.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '息州豪府', 'intro': '爆料了，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
         'src': 'images/4.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '时代广场', 'intro': '爆料，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
         'src': 'images/3.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '息州豪府', 'intro': '爆料了，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
         'src': 'images/1.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '息州豪府', 'intro': '爆料了，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
         'src': 'images/2.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '瀑布流', 'intro': '爆料了，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
         'src': 'images/3.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '瀑布流其实就是几个函数', 'intro': '爆料，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
         'src': 'images/4.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '瀑布流', 'intro': '爆料了，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
         'src': 'images/3.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '几个函数', 'intro': '爆料了，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
         'src': 'images/2.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
        {'title': '瀑布流函数', 'intro': '爆料了，苏亚雷斯又咬人啦，C罗哪有内马尔帅，梅西今年要不夺冠',
         'src': 'images/4.jpg', 'writer': 'sun', 'date': '2小时前', 'looked': 321},
    ]
    context={'sqlJson':sqlJson}
    return render(request,'excellentHouse.html',context)
def gotoJSON(request):
    return render(request,'testJSON.html')
def testJSON(request):
    year=request.GET.get('year')
    print(year)
    data={'url':"www.testJSON.com",'name':'sunlei'}
    return JsonResponse(data);


