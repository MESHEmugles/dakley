# Generated by Django 4.1.4 on 2022-12-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_alter_aboutme_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='aboutyu',
            field=models.TextField(blank=True, null=True),
        ),
    ]
