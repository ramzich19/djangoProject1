# Generated by Django 3.1.5 on 2021-05-21 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20210218_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zayavka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=120, null=True, verbose_name='описание')),
                ('email', models.EmailField(blank=True, max_length=120, null=True, verbose_name='email')),
                ('phone', models.CharField(max_length=11, verbose_name='Telephone')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]