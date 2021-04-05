# Generated by Django 3.1.3 on 2021-04-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='article',
            name='view_count',
            field=models.BigIntegerField(default=0, verbose_name='阅读数量'),
        ),
    ]