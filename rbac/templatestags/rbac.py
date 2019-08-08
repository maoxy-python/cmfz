from django.template import Library

from cmfz import settings

register = Library()


@register.inclusion_tag('static_rbac/static_menu.html')
def static_menu(request):
    """
    创建一级菜单
    :return: 
    """
    menu_list = request.session.get(settings.MENU_SESSION_KEY)
    return {"menu_list": menu_list}