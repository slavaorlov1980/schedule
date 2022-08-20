from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birthday = models.DateField('День рождения')
#    name = models.CharField(max_length=100)
#    login = models.CharField(max_length=50)
#    password = models.CharField(max_length=50)
#    type = models.OneToOneField(...)
    class Meta:
        verbose_name = 'Инфо пользователя'
        verbose_name_plural = 'Инфо пользователей'
        ordering = ['user']

    def __str__(self):
        return self.user.username

class Interval(models.Model):

    start_date = models.DateTimeField('Начало интервала')
    end_date = models.DateTimeField('Конец интервала')
    type = models.CharField('Тип пользователя', max_length=50)
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Ученик')
    
    class Meta:
        verbose_name = 'Интервал'
        verbose_name_plural = 'Интервалы'
        ordering = ['start_date']

class Event(models.Model):

    event_date = models.OneToOneField(Interval, on_delete=models.CASCADE, primary_key=True, verbose_name='Дата занятия')
    topic = models.CharField('Тема занятия', max_length=250)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher', verbose_name='Учитель')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student', verbose_name='Ученик')

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
        ordering = ['event_date']
