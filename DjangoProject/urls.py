# C:\Users\ZicE\PycharmProjects\DjangoProject\DjangoProject\urls.py

from django.contrib import admin
from django.urls import path, include # Убедитесь, что 'include' здесь
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # ЭТА СТРОКА ДОЛЖНА БЫТЬ
]

# Только для режима разработки: обслуживание медиафайлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)