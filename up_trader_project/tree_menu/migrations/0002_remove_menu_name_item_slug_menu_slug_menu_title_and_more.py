# Generated by Django 4.2 on 2023-04-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='name',
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='default slug', max_length=255, verbose_name='Item slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.SlugField(default='default slug', max_length=255, verbose_name='Menu slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='title',
            field=models.CharField(default='menu', max_length=255, unique=True, verbose_name='Menu title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Item name'),
        ),
    ]
