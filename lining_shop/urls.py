# lining_shop/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop import views


urlpatterns = [
    path('admin/', admin.site.urls),  # Стандартная админка Django
    path('', include('shop.urls', namespace='shop')),
    path('catalog/', views.catalog_page, name='catalog'),

path('cart/checkout/', views.checkout, name='checkout'),]

# Это нужно, чтобы Django умел показывать картинки кроссовок из папки media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)