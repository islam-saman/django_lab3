# Generated by Django 4.2 on 2023-04-21 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='track',
            new_name='department',
        ),
    ]
