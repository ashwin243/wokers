# services/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('service/<int:service_id>/', views.service_list, name='service_list'),
    path('worker/<int:worker_id>/', views.worker_detail, name='worker_detail'),
    path('worker/<int:worker_id>/book/', views.book_worker, name='book_worker'),
]
