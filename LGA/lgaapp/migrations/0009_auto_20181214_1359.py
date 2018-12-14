# Generated by Django 2.1.4 on 2018-12-14 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lgaapp', '0008_auto_20181214_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cipher',
            field=models.IntegerField(default=None, max_length=30, verbose_name='Шифр книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='groups',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Групи'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(default=None, max_length=30, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Мова'),
        ),
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.IntegerField(default=None, max_length=30, verbose_name='Серія'),
        ),
        migrations.AlterField(
            model_name='book',
            name='subject',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Тематика'),
        ),
    ]