# Generated by Django 3.1.4 on 2021-01-22 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twittereb', '0009_auto_20210122_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tw_tweet',
            name='image_path',
            field=models.CharField(blank=None, max_length=100, null=True),
        ),
    ]
