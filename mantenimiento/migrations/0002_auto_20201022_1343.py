# Generated by Django 3.0.5 on 2020-10-22 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sector',
            old_name='Servicio',
            new_name='servicio',
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('telefono', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.Servicio')),
            ],
        ),
    ]
