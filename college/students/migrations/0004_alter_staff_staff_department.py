# Generated by Django 3.2 on 2022-01-31 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_staff_staff_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staff_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='students.department'),
        ),
    ]
