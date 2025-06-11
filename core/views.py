from django.shortcuts import render
from .models import Project

def home_view(request):
    context = {
        'name': "ZicE", # <--
        'title': "Backend Developer",
        'description': "Привет! Я Роман, Backend разработчик. Я специализируюсь на разработке сайтов с использованием Jango, CSS и HTML. Моя цель - создавать эффективные и масштабируемые решения. Люблю решать сложные задачи и постоянно учусь новому. Готов к интересным проектам и сотрудничеству!",
        'email': "romaswat666@gmail.com",
        'phone': "+7(963)860-46-25",
        'github_link': "https://github.com/ZicESSS",
        'profile_image': 'static/images/profile.jpg',
    }
    return render(request, 'core/home.html', context)

def portfolio_view(request):
    projects = Project.objects.all()

    projects_with_delays = []
    base_delay = 1.2
    delay_increment = 0.1

    for i, project in enumerate(projects):

        project.animation_delay = f"{base_delay + i * delay_increment:.1f}s"

        projects_with_delays.append(project)


    context = {
        'projects': projects_with_delays,
        'page_title': 'Мои работы и проекты'
    }
    return render(request, 'core/portfolio.html', context)