# Generated by Django 3.2.9 on 2021-12-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restau', '0002_auto_20211201_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='dish',
        ),
        migrations.AddField(
            model_name='dish',
            name='pictures',
            field=models.ManyToManyField(to='restau.Picture'),
        ),
    ]
