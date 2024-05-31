from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('category_detail/<int:category_id>/', views.category_detail, name='category_detail')
]