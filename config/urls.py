from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from config.settings import MEDIA_ROOT, STATIC_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]

urlpatterns += static(settings.MEDIA_URL, serve , document_root = MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, serve, document_root = STATIC_ROOT)
