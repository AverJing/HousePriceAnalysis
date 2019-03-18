from django.shortcuts import render
from django.http import JsonResponse
from main.models import User
# Create your views here.
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
    return render(request,'index2.html')
