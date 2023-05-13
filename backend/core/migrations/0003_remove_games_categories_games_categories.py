# Generated by Django 4.2 on 2023-05-13 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_categories_games_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='categories',
        ),
        migrations.AddField(
            model_name='games',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='core.categories', verbose_name='Категория'),
        ),
    ]
