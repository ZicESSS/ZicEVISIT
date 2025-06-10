# C:\Users\ZicE\PycharmProjects\DjangoProject\core\urls.py

from django.urls import path
from . import views # Убедитесь, что 'views' импортированы

urlpatterns = [
    path('', views.home_view, name='home'), # Главная страница
    path('portfolio/', views.portfolio_view, name='portfolio'), # ЭТА СТРОКА ДОЛЖНА БЫТЬ
]