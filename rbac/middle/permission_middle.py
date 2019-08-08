import re

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from cmfz import settings


class CheckPermission(MiddlewareMixin):
    """
    用户权限信息的校验
    """
    def process_request(self, request):
        """
        当用户请求刚进入的时候出发执行
        :param request:
        :return:
        """
        """
        1. 获取当前用户请求的url
        2. 获取当前用户在session中保存的权限列表['/customer/list', '用户所拥有的权限']
        3. 权限信息的匹配
        """

        current_url = request.path_info

        for valid_url in settings.VALID_URL_LIST:
            if re.match(valid_url, current_url):
                # 白名单中的请求  无须验证
                # 返回None代表不拦截，直接执行视图函数
                return None

        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)

        print(current_url, permission_list)

        if not permission_list:
            return HttpResponse("请登录")

        flag = False

        for url in permission_list:
            reg = "^%s$" % url
            if re.match(reg, current_url):
                flag = True
                break

        # 代表有权访问
        if not flag:
            return HttpResponse("无权访问")




