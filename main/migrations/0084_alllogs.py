# Generated by Django 3.2.6 on 2023-12-18 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0083_rename_managerdecision_managermainhrdecision'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logs', models.TextField()),
                ('applicant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.jobapplication')),
            ],
        ),
    ]