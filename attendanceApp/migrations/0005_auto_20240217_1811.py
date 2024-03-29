# Generated by Django 3.2.7 on 2024-02-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceApp', '0004_auto_20240215_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='leave',
            name='start_date',
        ),
        migrations.AddField(
            model_name='leave',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='leavetype',
            name='cut_payement',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='leavetype',
            name='short_name',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
