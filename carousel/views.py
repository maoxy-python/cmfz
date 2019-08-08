import datetime
import json
import uuid

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from article.models import Carousel


def query_carousel(request):

    rows = []
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')
    # print(page_num,type(page_num), row_num,type(row_num))

    banner = Carousel.objects.all().order_by('id')
    all_page = Paginator(banner, row_num)
    page = Paginator(banner, row_num).page(page_num).object_list

    for i in page:
        rows.append(i)

    page_data = {"total": all_page.num_pages,
                 "records": all_page.count,
                 "page": page_num,
                 "rows": rows
                 }

    def myDefault(u):
        if isinstance(u, Carousel):
            return {'id': u.id,
                    'title': u.title,
                    'status': u.status,
                    'url': str(u.url),
                    'createDate': u.create_date.strftime('%Y-%m-%d'),
                    'description': u.description,
                    }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)


def index(request):

    return render(request, 'carousel/main.html')


@csrf_exempt
def edit_Banner(request):

    id = request.POST.get('id')
    title = request.POST.get('title')
    status = request.POST.get('status')
    description = request.POST.get('description')
    oper = request.POST.get('oper')
    if oper == 'edit':
        banner = Carousel.objects.get(pk=id)
        banner.title = title
        banner.description = description
        banner.status = status
        # banner.url = url
        banner.save()
    elif oper == 'add':
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        u_id = str(uuid.uuid4())

        d = {'bannerId': u_id}
        bannerId = json.dumps(d)

        print(type(bannerId), bannerId)

        Carousel.objects.create(id=u_id, title=title, status=status, description=description, create_date=now)
        return JsonResponse(d)
    elif oper == 'del':
        Carousel.objects.get(pk=id).delete()

    return HttpResponse()


def demo(request):

    return render(request, 'carousel/demo.html')


@csrf_exempt
def upload_file(request):

    pic = request.FILES.get('upload_pic1')
    name = request.POST.get('upload_title1')
    status = request.POST.get('upload_status1')
    title = request.POST.get('upload_name1')
    u_id = str(uuid.uuid4())
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    print(pic, name, status, title)
    Carousel.objects.create(id=u_id, url=pic, title=title, description=name, status=status, create_date=now)

    return HttpResponse()


