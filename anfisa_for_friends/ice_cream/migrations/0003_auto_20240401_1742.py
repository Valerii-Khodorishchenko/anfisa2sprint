# Generated by Django 3.2.16 on 2024-04-01 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_auto_20240331_1134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'текущую категорию', 'verbose_name_plural': 'Каетегории'},
        ),
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name': 'экземпляр добавки', 'verbose_name_plural': 'Добавки'},
        ),
        migrations.AlterModelOptions(
            name='wrapper',
            options={'verbose_name': 'экземпляр обёртки', 'verbose_name_plural': 'Обёртки'},
        ),
        migrations.AddField(
            model_name='icecream',
            name='output_order',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения'),
        ),
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wrapper',
            name='title',
            field=models.CharField(help_text='Уникальное название обёрткиб не более 256 символов', max_length=256, verbose_name='Название'),
        ),
    ]