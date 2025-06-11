# C:\Users\ZicE\PycharmProjects\DjangoProject\core\models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='project_images/', verbose_name="Изображение", blank=True, null=True)
    github_link = models.URLField(max_length=200, blank=True, verbose_name="Ссылка на GitHub")
    live_link = models.URLField(max_length=200, blank=True, verbose_name="Ссылка на демо")
    order = models.IntegerField(default=0, verbose_name="Порядок отображения") # Для сортировки проектов
    created_at = models.DateTimeField(auto_now_add=True) # Дата создания записи

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['order', '-created_at'] # Сортируем по порядку, затем по дате

    def __str__(self):
        return self.title