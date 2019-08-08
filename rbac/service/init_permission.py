from cmfz import settings


def init_permission(user, request):
    """
    用户权限的初始化
    :param user:
    :param request:
    :return:
    """

    # 2. 权限信息的初始化
    # 获取菜单相关的信息   title  is_menu  icon
    role_list = user.roles.filter(permissions__isnull=False).values('permissions__id',
                                                                    'permissions__url',
                                                                    'permissions__title',
                                                                    'permissions__is_menu',
                                                                    'permissions__icon',).distinct()

    # 获取权限中所有的url并且保存到列表中
    # permission_list = []
    # for item in role_list:
    #     permission_list.append(item['permissions__url'])

    # 3. 权限+ 菜单信息的初始化
    menu_list = []
    permission_list = []
    for item in role_list:
        # 在一个循环中完成权限和菜单的获取，不再使用列表生成式
        if item['permissions__is_menu']:
            permission_list.append(item['permissions__url'])
            temp = {
                'title': item['permissions__title'],
                'icon': item['permissions__icon'],
                'url': item['permissions__url'],
            }
            menu_list.append(temp)

    # 列表生成式
    # permission_list = [item['permissions__url'] for item in role_list]

    # 将权限保存到session中
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    # 将菜单的权限保存到session中
    request.session[settings.MENU_SESSION_KEY] = menu_list
