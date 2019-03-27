from django.shortcuts import render,redirect
from django.http import JsonResponse
from main.models import User
import json
import requests
# Create your views here.
def index(request, location=""):
    ip = request.META['REMOTE_ADDR']
    url = "http://whois.pconline.com.cn/ipJson.jsp?ip=%s&json=true" % ip
    a = requests.get(url=url)
    info = json.loads(a.text)
    result = '苏州'
    try:
        if info["city"] != '':
            result = info["city"].split('市')[0]
    except:
        pass

    if location != "":
        return render(request,'index.html', {'location':location})
    else:
        return render(request,'index.html', {'location':result})

def selectCity(request):
    return render(request, 'cityTest.html')

def main_html(request):
    return render(request,'index.html')

def new_login(request):
    return render(request,'Newlogin.html')

def new_register(request):
    return render(request,'register.html')
    
def login(request):
    username = request.POST.get('username')  # request.POST.get('name')也可以获取
    password = request.POST.get('password')

    # user=User.objects.get(name=username,password=password)
    try:
        user = User.objects.get(name=username)
    except:
        return JsonResponse({'res': 0})

    if user.password == password:
        request.session['username'] = username
        request.session['islogin'] = True
        return JsonResponse({'res': 1})
    return JsonResponse({'res': 0})

def logout(request):
    if not request.session.get('islogin', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/")

def ajaxregister(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirmpassword= request.POST.get('confirmpassword')
    email= request.POST.get('email')
    evername=User.objects.filter(name=username)
    if evername:
        return JsonResponse({'res': 1})#用户名冲突
    if  password!=confirmpassword:
        return JsonResponse({'res': 2})#两次密码不一致
    else:
      u=User()
      u.name=username
      u.password=password
      u.email=email
      u.save()
      print("注册成功")
      return JsonResponse({'res': 3})#成功
def indexAddEcharts(request):
    return render(request,'index.html')
