# Generated by Django 4.1.4 on 2022-12-14 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogstory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutorial',
            options={'managed': True, 'verbose_name': 'Tutorial', 'verbose_name_plural': 'Tutorial'},
        ),
    ]