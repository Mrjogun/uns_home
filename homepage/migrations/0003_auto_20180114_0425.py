# Generated by Django 2.0.1 on 2018-01-13 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_remove_profile_student_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='student_year',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
