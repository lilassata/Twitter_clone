# Generated by Django 3.0.1 on 2022-10-03 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='likes'),
        ),
    ]