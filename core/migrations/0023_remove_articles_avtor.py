# Generated by Django 3.1.5 on 2021-02-16 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_comments_user_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='avtor',
        ),
    ]
