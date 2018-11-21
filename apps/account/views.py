from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.db.models import Q
from django.shortcuts import render, redirect
from django.template import loader

from apps.account.models import User

# check_password
# 第一种请求直接通过登录路径访问
# 需要登录验证的接口跳转登录界面 ?next=/account/update/
from django_movies import settings


def login_view(request):
    if request.method == 'GET':
        next = request.GET.get('next')
        return render(request, 'login.html', context={'next': next})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')
        if username and password:
            # 请输入用户名或者邮箱或者手机号
            # Q(username=username) | Q(phone=phone) | Q(email=email)
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    # 表示登录成功
                    # 记住登录状态
                    login(request, user)
                    next = next if next else '/'
                    return redirect(next)
                else:
                    return render(request, 'login.html', {'msg': '您的账号已被警用!!!请与管理员联系'})
            else:
                return render(request, 'login.html', {'msg': '账号密码输入有误'})
        else:
            return render(request, 'login.html', {'msg': '账号密码不能为空!!!'})
    else:
        # 不支持的请求方式
        return render(request, 'error/404.html')


#  发送邮件激活
#  注册通过之后 is_active = 0
#  发送邮件
#  用户点击激活链接
#  访问我们服务器指定的接口(激活的接口)
#  修改当前用户的激活的状态    is_active = 1

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            if username and password and phone:
                #     注册
                user = User.objects.filter(Q(username=username) | Q(phone=phone))
                if user.exists():
                    print('用户名或者手机号已经被注册')
                else:
                    # 保存用户的操作
                    user = User.objects.create_user(username=username, password=password, phone=phone, email=email,
                                                    is_active=0)
                    if user:
                        # 如果注册成功  直接记住用户登录状态,跳转首页
                        #               跳转登录界面,让用户重新登录一次
                        # 记住用户状态
                        # 底层做了两个操作,
                        # 第一个操作将用户信息保存到session中
                        # 第二个操作将用户信息绑定到request对象
                        # request.user
                        active_url = f'http://127.0.0.1:8000/account/active/?uid={user.id}'
                        content = loader.render_to_string('mail.html',
                                                          request=request,
                                                          context={'username': username, 'active_url': active_url})
                        send_active_mail(subject='91电影网激活邮件', content=content, to=[email])
                        return redirect('/')
                    # 用户注册成功
                    else:
                        pass
        #                注册失败
        except Exception as e:
            return render(request, 'error/404.html')


# xxx/active/?uid=1
def active_account(request):
    uid = request.GET.get('uid')
    User.objects.filter(id=uid).update(is_active=1)
    return redirect('/')


@login_required()
def logout_view(request):
    # 退出登录
    logout(request)
    return redirect('/')


# 验证用户是否登录

@login_required()
def update(request):
    user = request.user
    user.save()
    return redirect('/')


def detail(request):
    pass


def hello_mail(request):
    """
        subject,标题
        message, 邮件的内容
        from_email,发送邮件者
        recipient_list,  接受邮件列表
        html_message = 邮件的内容,以html格式显示邮件内容
    :param request:
    :return:
    """
    # send_mail(subject='xxx线上xxx注册邮件',
    #           message='注册成功可以观看更多高清无码的xxx',
    #           from_email=settings.EMAIL_HOST_USER,
    #           recipient_list=['18614068889@163.com']
    #           )
    content = loader.render_to_string('mail.html', request=request)
    send_mail(subject='xxx线上xxx注册邮件',
              message='',
              html_message=content,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=['18614068889@163.com']
              )

    return render(request, 'msg.html')


def send_active_mail(subject='', content=None, to=None):
    send_mail(subject=subject,
              message='',
              html_message=content,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=to
              )
