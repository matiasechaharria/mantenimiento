# Generated by Django 3.0.5 on 2020-10-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preventivo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preventivo',
            name='fecha',
            field=models.DateField(),
        ),
    ]
