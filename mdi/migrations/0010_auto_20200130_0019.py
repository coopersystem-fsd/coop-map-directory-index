# Generated by Django 3.0.2 on 2020-01-30 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0009_organization_activities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]