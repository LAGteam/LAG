# Generated by Django 2.1.2 on 2018-12-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lgaapp', '0005_auto_20181213_1635'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='art',
            options={'ordering': ['name'], 'verbose_name': 'Мистецтво', 'verbose_name_plural': 'Мистецтво'},
        ),
        migrations.RemoveField(
            model_name='art',
            name='country',
        ),
        migrations.AlterField(
            model_name='art',
            name='name',
            field=models.CharField(db_index=True, max_length=200, unique=True),
        ),
    ]
