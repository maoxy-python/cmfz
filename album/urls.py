from django.urls import path, include

from album import views

urlpatterns = [
    path('getAllAlbum/', views.getAllAlbum),
    path('getChapter/', views.getChapterByAlbumId),
    path('addChapter/', views.addChapter),
]