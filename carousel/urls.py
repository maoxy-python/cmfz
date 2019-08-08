from django.urls import path

from carousel import views

urlpatterns = [
    path('query/', views.query_carousel),
    path('index/', views.index),
    path('demo/', views.demo),
    path('upload_file/', views.upload_file),
    path('editBanner/', views.edit_Banner),
]

