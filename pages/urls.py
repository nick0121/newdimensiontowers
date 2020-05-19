from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('accessories', views.accessories, name="accessories"),
    path('accessories/<query>/', views.accessory, name="accessory"),
    path('accessories/<slug:category>/<slug:product_id>/', views.accessory_product, name="accessory_product"),
    path('biminis', views.biminis, name="biminis"),
    path('installation', views.installation, name="installation"),
    path('faq', views.faq, name="faq"),
    path('orders', views.orders, name="orders"),
    path('product', views.product, name="product"),
]