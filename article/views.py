import json
from datetime import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from carousel.models import Article


# @cache_page(60*60, key_prefix='getAll')
def getALLArticle(request):

    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    article = Article.objects.all().order_by('id')
    all_page = Paginator(article, row_num)
    page = Paginator(article, row_num).page(page_num).object_list

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    for i in page:
        rows.append(i)

    def myDefault(u):
        if isinstance(u, Article):
            return {'id': u.id,
                    'content': u.content,
                    'title': u.title,
                    'status': u.status,
                    'createDate': u.create_date.strftime('%Y-%m-%d'),
                    'publishDate': u.publish_date.strftime('%Y-%m-%d'),
                    }
    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)


@csrf_exempt
def editArticle(request):
    """
    点击文章修改后的方法，需要将副文本的内容保存到数据库
    :param request:
    :return:
    """
    title = request.POST.get("title")
    status = request.POST.get("status")
    content = request.POST.get("content")
    article_Id = request.GET.get("articleId")
    print(title, status, content, article_Id)

    article = Article.objects.get(pk=article_Id)
    article.content = content
    article.title = title
    article.status = status
    article.save()

    return HttpResponse()


@csrf_exempt
def uploadInsertImg(request):

    """
    解决富文本编辑器图片上传的方法  将图片的绝对路径保存到数据库的方法
    :param request:
    :return:
    """

    file = request.FILES.get('imgFile')

    # path = default_storage.save('static/upload/image/11111.jpg', ContentFile(file.read()))
    # print(path)

    if file:
        img_real = request.scheme+"://"+request.get_host()+"/static/upload/img/"+str(file)
        print(img_real)
        result = {'error': 0, "url": img_real}
        article = Article.objects.get(pk="1")
        article.new_img = file
        article.save()
    else:
        result = {'error': 1, "message": "上传出错"}

    return HttpResponse(json.dumps(result), content_type="application/json")


def addArticle(request):
    """
    点击添加文章后处理的视图
    :param request:
    :return:
    """
    title = request.GET.get("title")
    status = request.GET.get("status")
    content = request.GET.get("content")
    now = datetime.now().strftime('%Y-%m-%d')
    print(title, status, content)
    Article.objects.create(pk="1", title=title, status=status, content=content, create_date=now, publish_date=now)

    return HttpResponse()


def delArticle(request):
    """
    删除按钮
    :param request:
    :return:
    """
    art_id = request.GET.get('articleId')
    print(request.GET, art_id)
    Article.objects.get(pk=art_id).delete()

    return HttpResponse()
