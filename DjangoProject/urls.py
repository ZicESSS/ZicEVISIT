# /home/ZicE/mysite/DjangoProject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # Маршрут для админ-панели Django
    path('', include('core.urls')),  # <--- Ключевая строка: включает URL-ы из вашего приложения 'core'.
                                     # Если ваше приложение называется не 'core', измените 'core.urls' на 'ваше_приложение.urls'
]

# Важное примечание: Эти строки НУЖНЫ для локальной разработки (DEBUG=True)
# для отдачи статики и медиа. На PythonAnywhere в режиме продакшена (DEBUG=False)
# статические и медиафайлы отдаются самой платформой PythonAnywhere,
# поэтому этот блок кода НЕ АКТИВИРУЕТСЯ, когда DEBUG=False.
# Однако, его можно оставить для удобства локальной разработки.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)