# Generated by Django 3.2.9 on 2021-12-03 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restau', '0003_auto_20211203_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='name',
            field=models.CharField(default='Burger', max_length=30),
            preserve_default=False,
        ),
    ]
