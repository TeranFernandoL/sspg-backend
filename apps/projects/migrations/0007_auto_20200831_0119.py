# Generated by Django 2.2.3 on 2020-08-31 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200830_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='adviser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_adviser', to='faculties.Teacher'),
        ),
        migrations.AlterField(
            model_name='project',
            name='jury_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_jury1', to='faculties.Teacher'),
        ),
        migrations.AlterField(
            model_name='project',
            name='jury_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_jury2', to='faculties.Teacher'),
        ),
        migrations.AlterField(
            model_name='project',
            name='jury_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_jury3', to='faculties.Teacher'),
        ),
        migrations.AlterField(
            model_name='project',
            name='student_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_student1', to='faculties.Student'),
        ),
        migrations.AlterField(
            model_name='project',
            name='student_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_student2', to='faculties.Student'),
        ),
        migrations.AlterField(
            model_name='project',
            name='student_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_student3', to='faculties.Student'),
        ),
    ]
