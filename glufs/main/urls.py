from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('overview/', views.overview, name='overview'),
    path('detail/<int:meal_id>/', views.detail, name='detail'),
    path('create/', views.create_meal, name='create_meal'),
    path('create_label/', views.create_label, name='create_label'),
]
