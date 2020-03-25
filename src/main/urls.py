from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

from main.views.overview import ViewOverview

urlpatterns = [
#    url(r'^$', views.index, name='index'),
    path('overview/', login_required(ViewOverview.as_view()), name='overview'),
#    path('detail/<int:meal_id>/', views.detail, name='detail'),
#    path('create/', views.create_meal, name='create_meal'),
#    path('edit_meal/<int:meal_id>/', views.edit_meal, name='edit_meal'),
#    path('create_label/', views.create_label, name='create_label'),
#    path('edit_label/<int:label_id>/', views.edit_label, name='edit_label'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
