# Generated by Django 3.2.6 on 2023-12-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0075_alter_managerdecision_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='mainHr_is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
