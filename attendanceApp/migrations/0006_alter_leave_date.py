# Generated by Django 3.2.7 on 2024-02-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceApp', '0005_auto_20240217_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]