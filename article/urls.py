from django.urls import path

from article import views

urlpatterns = [
    path('getALLArticle/', views.getALLArticle),
    path('uploadInsertImg/', views.uploadInsertImg),
    path('editArticle/', views.editArticle),
    path('addArticle/', views.addArticle),
    path('delArticle/', views.delArticle),
]

