# Generated by Django 3.1.5 on 2021-02-16 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='articles',
            name='name_kk',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='articles',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='articles',
            name='text1_en',
            field=models.TextField(blank=True, null=True, verbose_name='Текст1'),
        ),
        migrations.AddField(
            model_name='articles',
            name='text1_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Текст1'),
        ),
        migrations.AddField(
            model_name='articles',
            name='text1_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Текст1'),
        ),
        migrations.AddField(
            model_name='articles',
            name='text2_en',
            field=models.TextField(blank=True, null=True, verbose_name='Текст2'),
        ),
        migrations.AddField(
            model_name='articles',
            name='text2_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Текст2'),
        ),
        migrations.AddField(
            model_name='articles',
            name='text2_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Текст2'),
        ),
        migrations.AddField(
            model_name='articles',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='articles',
            name='text_kk',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='articles',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
    ]
