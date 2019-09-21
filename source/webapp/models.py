from django.db import models

STATUS_CHOICES = (
    ('active', 'Активно'),
    ('blocked', 'Заблокировано')
)


class Entry(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Почта')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    status = models.CharField(max_length=20, verbose_name='Статус',
                                choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    def __str__(self):
        return self.name


