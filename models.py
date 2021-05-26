from django.db import models


class Articles(models.Model):
    name = models.CharField('Ім\'я', max_length=30)
    surname = models.CharField('Прізвище', max_length=30)
    phone = models.CharField('Номер телефону ', max_length=20)
    email = models.CharField('Пошта', max_length=30)
    password = models.CharField('Пароль', max_length=20)

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'


