# Generated by Django 2.2.3 on 2020-09-09 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0003_auto_20200828_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.CharField(blank=True, choices=[('PREGRADO', 'PREGRADO'), ('POSGRADO', 'POSGRADO')], max_length=50, null=True, verbose_name='Grado'),
        ),
    ]
