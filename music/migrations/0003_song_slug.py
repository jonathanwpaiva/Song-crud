# Generated by Django 3.1.7 on 2021-02-21 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20210220_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.SlugField(default='music', max_length=255, unique=True),
        ),
    ]