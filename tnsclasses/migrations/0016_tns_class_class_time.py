# Generated by Django 3.1.2 on 2021-01-24 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tnsclasses', '0015_remove_tns_class_class_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='tns_class',
            name='class_time',
            field=models.TimeField(default='12:10'),
        ),
    ]