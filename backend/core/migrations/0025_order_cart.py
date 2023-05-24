# Generated by Django 4.2 on 2023-05-21 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_image_alter_profile_user'),
        ('core', '0024_alter_review_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(blank=True, default=0, editable=False, null=True, verbose_name='Итого')),
                ('game', models.ManyToManyField(to='core.games', verbose_name='Игры')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.profile', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(blank=True, default=0, editable=False, null=True, verbose_name='Итого')),
                ('game', models.ManyToManyField(to='core.games', verbose_name='Игры')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.profile', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
    ]