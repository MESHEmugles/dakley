# Generated by Django 4.1.4 on 2023-07-20 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogstory', '0003_address_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialcomment',
            name='comment_tuto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogstory.tutorial'),
        ),
    ]
