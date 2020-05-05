from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

from main.views.overview import ViewOverview
from main.views.detail import ViewDetail
from main.views.create_meal import ViewCreateMeal
from main.views.edit_meal import ViewEditMeal
from main.views.create_label import ViewCreateLabel
from main.views.edit_label import ViewEditLabel
from main.views.make_plans import ViewMakePlans
from main.views.plan_week import ViewPlanWeek

urlpatterns = [
    path('overview/', ViewOverview.as_view(), name='overview'),
    path('detail/<int:meal_id>/', ViewDetail.as_view(), name='detail'),
    path('create/', ViewCreateMeal.as_view(), name='create_meal'),
    path('edit_meal/<int:meal_id>/', ViewEditMeal.as_view(), name='edit_meal'),
    path('create_label/', ViewCreateLabel.as_view(), name='create_label'),
    path('edit_label/<int:label_id>/', ViewEditLabel.as_view(), name='edit_label'),
    path('make_plans/', ViewMakePlans.as_view(), name='make_plans'),
    path('plan_week/', ViewPlanWeek.as_view(), name='plan_week'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = [
#     path('overview/', login_required(ViewOverview.as_view()), name='overview'),
#     path('detail/<int:meal_id>/', login_required(ViewDetail.as_view()), name='detail'),
#     path('create/', login_required(ViewCreateMeal.as_view()), name='create_meal'),
#     path('edit_meal/<int:meal_id>/', login_required(ViewEditMeal.as_view()), name='edit_meal'),
#     path('create_label/', login_required(ViewCreateLabel.as_view()), name='create_label'),
#     path('edit_label/<int:label_id>/', login_required(ViewEditLabel.as_view()), name='edit_label'),
#     path('make_plans/', login_required(ViewMakePlans.as_view()), name='make_plans'),
#     path('plan_week/', login_required(ViewPlanWeek.as_view()), name='plan_week'),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

