# Generated by Django 4.2 on 2023-05-16 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_games_release_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterfaceLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=255, verbose_name='Язык')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
            },
        ),
        migrations.AlterField(
            model_name='games',
            name='interface_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.interfacelanguage', verbose_name='Язык интерфейса'),
        ),
    ]