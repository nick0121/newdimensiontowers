from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="towers"),
    # path('tower/', views.towers_view, name="towers_view"),
    path('<slug:manufacturer_name>/', views.tower_manufacturer, name="tower_manufacturer"),
    path('<slug:manufacturer_name>/<slug:boat_id>/', views.tower_product, name="tower_product"),
]

