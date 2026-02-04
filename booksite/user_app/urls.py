from django.urls import path
from .views import *

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', register_view, name='register')]
