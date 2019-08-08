import json

import xlwt
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from carousel.models import User
from rbac.models import UserInfo
from rbac.service.init_permission import init_permission


def getRegister(request):

    user = User.objects.all()
    rows = []

    data = {'name': ["一", "二", "三", "四", "五", "六", "七"], 'value': [12, 34, 45, 21, 56, 43, 41]}

    for i in user:
        rows.append(i)

    def myDefault(u):
        if isinstance(u, User):
            return {'name', u.name}

    # data = json.dumps(rows, default=myDefault)

    data_list = json.dumps(data, ensure_ascii=False)
    print(data_list)

    return HttpResponse(data_list)


def getMap(request):

    data = [{'name': '北京', 'value': 1234}, {'name': '上海', 'value': 2345},
            {'name': '青海', 'value': 2565},
            {'name': '新疆', 'value': 245},
            {'name': '山西', 'value': 25},
            {'name': '河南', 'value': 2345},
            {'name': '河北', 'value': 6345},
            {'name': '四川', 'value': 7345},
            {'name': '重庆', 'value': 2345},
            {'name': '云南', 'value': 8345},
            {'name': "贵州", 'value': 9345},
            {'name': '黑龙江', 'value': 345},
            {'name': '吉林', 'value': 245},
            {'name': '海南', 'value': 235}]

    data_map = json.dumps(data, ensure_ascii=False)
    print(data_map)
    return HttpResponse(data_map)


@csrf_exempt
def login(request):
    # 1. 用户的登录
    if request.method == 'GET':
        return render(request, 'carousel/login.html')
    user = request.POST.get('name')
    pwd = request.POST.get('password')

    user = UserInfo.objects.filter(name=user, password=pwd).first()
    if not user:
        return render(request, 'carousel/login.html', {'msg': '用户名或密码不正确'})
    """
    # 根据当前用户信息获取此用户所拥有的的所有的权限，并放入session
    # 先获取当前用户所拥有的角色，根据角色获取权限 
    # role_list = user.roles.all()  再根据角色获取权限
    # 但django提供manyTo many的跨表查询,直接获取所有的权限
    # role_list = user.roles.all().values('permissions__url', 'permissions__url').distinct()
    
    # 当前设计有问题1：
        1. 一个用户是否可以有多个角色
        2. 一个角色是否可以拥有多个权限
        当这种情况出现的时候，查询出来的url有许多重复的所以需要去重
    问题2：
        当新添角色的时候，如果没有分配权限，则该用户对应的权限为null，
        # role_list = user.roles.filter(permissions__isnull=False  ).values('permissions__url', 'permissions__url').distinct()
    """

    init_permission(user, request)

    return redirect('/carousel/index/')
    # return HttpResponse()


def arrive_login(request):

    return render(request, 'carousel/login.html')
