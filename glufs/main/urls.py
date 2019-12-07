from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('overview/', views.overview, name='overview'),
    path('<int:meal_id>/', views.detail, name='detail'),
]
