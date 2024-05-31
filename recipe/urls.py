from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('category_detail/<int:category_id>/', views.category_detail, name='category_detail')
]