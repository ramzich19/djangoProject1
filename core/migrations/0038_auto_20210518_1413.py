# Generated by Django 3.1.5 on 2021-05-18 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_remove_articles_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='author',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='document',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='user_firstname',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='user_photo',
        ),
    ]
