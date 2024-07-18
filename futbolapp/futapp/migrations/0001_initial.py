# Generated by Django 5.0.6 on 2024-06-24 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('estadio', models.CharField(max_length=100)),
                ('fundacion', models.DateField()),
                ('presidente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('categoria', models.CharField(max_length=100)),
                ('fecha_contratacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.PositiveIntegerField()),
                ('posicion', models.CharField(max_length=50)),
                ('numero_camiseta', models.PositiveIntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futapp.equipo')),
                ('profesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='futapp.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_pago', models.CharField(choices=[('M', 'Mensualidad'), ('I', 'Inscripción')], max_length=1)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futapp.equipo')),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futapp.jugador')),
            ],
        ),
    ]