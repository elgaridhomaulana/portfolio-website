# Generated by Django 3.0.4 on 2020-03-21 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_created',
            field=models.DateField(),
        ),
    ]
