# Generated by Django 4.2.5 on 2023-09-28 11:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task3app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.date(2023, 9, 28)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_reg',
            field=models.DateField(default=datetime.date(2023, 9, 28)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_reg',
            field=models.DateField(default=datetime.date(2023, 9, 28)),
        ),
    ]
