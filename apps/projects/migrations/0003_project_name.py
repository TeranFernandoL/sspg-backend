# Generated by Django 2.2.3 on 2020-08-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre'),
        ),
    ]
