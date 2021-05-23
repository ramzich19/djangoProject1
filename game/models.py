
from django.db import models



class TopBack(models.Model):
    name = models.CharField('Name', max_length=120)
    description = models.CharField('описание', max_length=120, blank=True, null=True)
    email = models.EmailField('email', max_length=120, blank=True, null=True )
    phone = models.CharField('Telephone', max_length=11)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'





class Zayavka(models.Model):
    name = models.CharField('Name', max_length=120)
    description = models.CharField('Услуга', max_length=120, blank=True, null=True)
    email = models.EmailField('email', max_length=120, blank=True, null=True )
    phone = models.CharField('Telephone', max_length=11)


    def __str__(self):
        return f"{self.name} из услуг \"{self.description}\""

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
