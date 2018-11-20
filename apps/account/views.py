from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from apps.account.models import User


# check_password

def login_view(request):
    # 登录用户
    user = authenticate(username='qq123456', password='12345')
    # 上面只是验证用户名密码是否正确
    # 判断用户是否是激活状态
    if user.is_active:
        # 登录成功
        # 记住登录状态
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            if username and password and phone:
                #     注册
                user = User.objects.filter(Q(username=username) | Q(phone=phone))
                if user.exists():
                    print('用户名或者手机号已经被注册')
                else:
                    # 保存用户的操作
                    user = User.objects.create_user(username=username, password=password, phone=phone)
                    if user:
                        # 如果注册成功  直接记住用户登录状态,跳转首页
                        #               跳转登录界面,让用户重新登录一次
                        # 记住用户状态
                        # 底层做了两个操作,
                        # 第一个操作将用户信息保存到session中
                        # 第二个操作将用户信息绑定到request对象
                        login(request, user)
                        # request.user
                        return redirect('/')
                    # 用户注册成功
                    else:
                        pass
        #                注册失败
        except Exception as e:

            pass


@login_required()
def logout_view(request):
    # 退出登录
    logout(request)
    return redirect('/')


# 验证用户是否登录
@login_required(login_url='/account/login/')
def update(request):
    user = request.user
    user.save()
    return redirect('/')


def detail(request):
    pass
