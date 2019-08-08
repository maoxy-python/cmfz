from cmfz import settings


def init_permission(user, request):
    """
    用户权限的初始化
    :param user:
    :param request:
    :return:
    """

    # 2. 权限信息的初始化
    role_list = user.roles.filter(permissions__isnull=False).values('permissions__url', 'permissions__url').distinct()

    # 获取权限中所有的url并且保存到列表中
    # permission_list = []
    # for item in role_list:
    #     permission_list.append(item['permissions__url'])

    # 列表生成式
    permission_list = [item['permissions__url'] for item in role_list]

    # 将权限保存到session中
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
