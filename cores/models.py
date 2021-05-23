from django.db import models

# Create your models here.
class Articles(models.Model):
    date = models.DateField(verbose_name= 'Дата')
    name = models.CharField(max_length=200, verbose_name= 'Название')
    text = models.TextField(verbose_name='Текст')
    text1 = models.TextField(verbose_name='Текст1',blank=True)
    text2 = models.TextField(verbose_name='Текст2',blank=True)
    text3 = models.TextField(verbose_name='Текст3',blank=True)
    image = models.ImageField('Изображение', upload_to='images/', blank=None, null=True)
    image2 = models.ImageField('Изображение 2', upload_to='images/', blank=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name='Мероприятие'
        verbose_name_plural='Мероприятия'
