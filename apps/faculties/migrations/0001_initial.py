# Generated by Django 2.2.3 on 2020-08-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='Codigo')),
                ('type_document', models.CharField(blank=True, choices=[('DNI', 'DNI'), ('PASSPORT', 'PASSPORT'), ('INMIGRATION_CARD', 'INMIGRATION_CARD')], max_length=30, null=True, verbose_name='Tipo de Documento')),
                ('document', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nro Documento')),
                ('last_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Apellidos')),
                ('first_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Nombre')),
                ('email', models.EmailField(blank=True, max_length=60, null=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono')),
                ('address', models.CharField(blank=True, max_length=20, null=True, verbose_name='Direccion')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='faculties/students', verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('last_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Apellidos')),
                ('first_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Nombre')),
                ('email', models.EmailField(blank=True, max_length=60, null=True, verbose_name='Email')),
                ('type_document', models.CharField(blank=True, choices=[('DNI', 'DNI'), ('PASSPORT', 'PASSPORT'), ('INMIGRATION_CARD', 'INMIGRATION_CARD')], max_length=30, null=True, verbose_name='Tipo de Documento')),
                ('document', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nro Documento')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
            },
        ),
    ]
