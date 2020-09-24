# Generated by Django 2.2.3 on 2020-08-27 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(blank=True, max_length=30, null=True, verbose_name='Codigo')),
                ('state', models.CharField(blank=True, choices=[('RECEIVED', 'RECEIVED'), ('UNDER_REVIEW', 'UNDER_REVIEW'), ('COMPLETED', 'COMPLETED')], max_length=40, null=True, verbose_name='Estado')),
                ('type', models.CharField(blank=True, choices=[('TI', 'TI'), ('TESIS', 'TESIS'), ('TSP', 'TSP')], max_length=20, null=True, verbose_name='Tipo')),
                ('semester_1', models.BooleanField(default=False, verbose_name='Termino Semestre 1?')),
                ('qualification_1', models.FloatField(blank=True, null=True, verbose_name='Calificacion Semestre 1')),
                ('semester_2', models.BooleanField(default=False, verbose_name='Termino Semestre 2?')),
                ('qualification_2', models.FloatField(blank=True, null=True, verbose_name='Calificacion Semestre 2')),
                ('num_rd', models.CharField(blank=True, max_length=30, null=True, verbose_name='Numero de Resolucion Decanal')),
                ('date_register', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de registro')),
                ('date_doc', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Documento')),
                ('date_validity', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Vigencia')),
                ('date_supporting', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Sustentacion')),
                ('date_acceptance', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Aceptacion')),
                ('congress', models.CharField(blank=True, max_length=200, null=True, verbose_name='Congreso o Revista')),
                ('adviser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects_adviser', to='faculties.Teacher')),
                ('jury_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects_jury1', to='faculties.Teacher')),
                ('jury_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects_jury2', to='faculties.Teacher')),
                ('jury_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects_jury3', to='faculties.Teacher')),
                ('student_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects_student1', to='faculties.Student')),
                ('student_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects_student2', to='faculties.Student')),
                ('student_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects_student3', to='faculties.Student')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
    ]
