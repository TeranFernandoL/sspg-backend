# Generated by Django 2.2.3 on 2020-09-09 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0005_auto_20200909_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='codigo',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
