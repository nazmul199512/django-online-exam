# Generated by Django 3.1.4 on 2021-01-11 18:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 18, 5, 35, 643462, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='exam',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 18, 5, 35, 643462, tzinfo=utc)),
        ),
    ]
