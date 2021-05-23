from django.db import models
from django.contrib.auth.models import User
from .middleware import get_current_user
from django.db.models import Q
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64,verbose_name='название')
    image = models.ImageField('Photo', upload_to='images/', blank=True, null=True)
    text = models.TextField(verbose_name='Текст',blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'


class Articles(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория',blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Владелец статьи', blank=True,null=True)
    create_date = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=200, verbose_name= 'Название')
    text = models.TextField(verbose_name='Текст')
    price = models.CharField('email', max_length=120,null=True)

    ok = models.BooleanField("Опубликовать", default = False)

    image = models.ImageField('Photo', upload_to='images/', blank=True, null=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name='Статью'
        verbose_name_plural='Статьи'


class StatusFilterComments(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Q(status=False, author = get_current_user()) | Q(status=False, article__author=get_current_user()) | Q(status=True))

class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete= models.CASCADE, verbose_name='Статья', blank=True, null=True, related_name='comments_articles')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True)
    user_photo = models.CharField(max_length=200,null=True,verbose_name= 'фото')
    user_name = models.CharField(max_length=200,null=True,verbose_name= 'имя')
    user_firstname = models.CharField(max_length=200,null=True,verbose_name= 'фамилия')
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Текст комментария')
    status = models.BooleanField(verbose_name='Видимость статьи', default=False)
    objects = StatusFilterComments()
    def __str__(self):
        return str(self.article)


    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии'
