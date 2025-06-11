# /home/ZicE/mysite/core/views.py

from django.shortcuts import render
from django.conf import settings
from .models import Project # Импортируем вашу модель Project

def index(request):
    profile_data = getattr(settings, 'PROFILE_DATA', {})
    # Если вы используете проекты из БД на главной тоже, измените эту строку:
    # portfolio_projects = Project.objects.all()
    # А если из settings.py, то оставьте как есть:
    # portfolio_projects = getattr(settings, 'PORTFOLIO_PROJECTS', [])

    context = {
        'profile': profile_data,
        # 'projects': portfolio_projects, # Если проекты для главной нужны
        'page_title': 'Мой Сайт-Портфолио', # Добавьте это для главной страницы, если нужно
    }
    return render(request, 'core/home.html', context)

def portfolio(request):
    portfolio_projects = Project.objects.all() # Получаем все проекты из БД
    context = {
        'projects': portfolio_projects,
        'page_title': 'Мои работы', # <--- ДОБАВЬТЕ ЭТУ СТРОКУ для заголовка портфолио
    }
    return render(request, 'core/portfolio.html', context)