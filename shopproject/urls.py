from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from shopproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('shop.urls')),
    path('staff/', include('shop.urls_staff')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)