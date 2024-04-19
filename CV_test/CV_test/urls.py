from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', include('log_in.urls')),
    path('chat/', include('msgs.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
