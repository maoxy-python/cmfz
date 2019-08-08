import json

from django.core.paginator import Paginator
from django.http import HttpResponse

from mutagen.mp3 import MP3
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from carousel.models import Album, Chapter


def getAllAlbum(request):

    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    album = Album.objects.all().order_by('id')
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)

    for i in page:
        rows.append(i)

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, Album):
            return {
                "author": u.author,
                "brief": u.brief,
                "broadcast": u.broadcast,
                "count": u.count,
                "cover": u.cover,
                "createDate": u.create_date.strftime('%Y-%m-%d'),
                "id": u.id,
                "publishDate": u.publish_date.strftime('%Y-%m-%d'),
                "score": u.score,
                "status": u.status,
                "title": u.title,
            }
    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)


def getChapterByAlbumId(request):

    album_Id = request.GET.get('albumId')
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    album = Chapter.objects.all().filter(album_id=album_Id).order_by('id')
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)

    for i in page:
        rows.append(i)

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, Chapter):
            return {
                "albumId": u.album_id,
                "createDate": u.create_date,
                "duration": u.duration,
                "id": u.id,
                "size": u.size,
                "title": u.title,
                "url": u.url,
            }
    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)


@csrf_exempt
def addChapter(request):

    """
    添加章节的方法
    :param request:
    :return:
    """

    title = request.POST.get('upload_title')
    file = request.FILES.get('file_name')
    audio = MP3(file)
    duration = audio.info.length
    Chapter.objects.create(title=title, size=file.size, time=duration, audio=file)
    return HttpResponse()
