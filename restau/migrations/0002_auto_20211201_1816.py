# Generated by Django 3.2.9 on 2021-12-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restau', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='name',
        ),
        migrations.AlterField(
            model_name='owner',
            name='type',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Company', 'Company')], default='Individual', max_length=30),
        ),
    ]