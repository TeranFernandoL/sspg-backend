# Generated by Django 2.2.3 on 2020-08-30 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200830_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.CharField(blank=True, choices=[('PENDIENTE', 'PENDIENTE'), ('ACEPTADO', 'ACEPTADO'), ('SUSPENDIDO', 'SUSPENDIDO'), ('OBSERVADO', 'OBSERVADO'), ('ENTREGADO', 'ENTREGADO'), ('SUSTENTADO', 'SUSTENTADO')], max_length=40, null=True, verbose_name='Estado'),
        ),
    ]
