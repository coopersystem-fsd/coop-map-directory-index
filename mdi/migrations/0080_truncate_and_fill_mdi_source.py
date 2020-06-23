# Generated by Django 3.0.7 on 2020-06-23 17:34

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0079_move_source_to_mdi'),
    ]

    operations = [
        migrations.RunSQL('TRUNCATE mdi_source RESTART IDENTITY;'),
        migrations.RunSQL('INSERT INTO mdi_source (SELECT * FROM accounts_source);')
    ]
