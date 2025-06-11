# /home/ZicE/mysite/core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ДОЛЖНА БЫТЬ СТРОКА ДЛЯ ПОРТФОЛИО:
    path('portfolio/', views.portfolio, name='portfolio'), # <--- ДОБАВЬТЕ ЭТУ СТРОКУ, ЕСЛИ ЕЕ НЕТ!
    # Убедитесь, что имя 'portfolio' совпадает с тем, что вы используете в шаблоне.
    # Путь 'portfolio/' может быть любым, например, 'my-portfolio/'
]