from django.urls import path
from .views import index
from django.views import View
from . import views

urlpatterns = [
    path('book/', index, name='index'),
    path('', views.upload_images, name='upload'),
    path('delete/<int:img_id>/', views.delete_image, name='delete_image'),

]
