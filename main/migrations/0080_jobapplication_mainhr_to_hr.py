# Generated by Django 3.2.6 on 2023-12-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0079_alter_emaillog_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='mainHr_to_hr',
            field=models.BooleanField(default=False),
        ),
    ]