# Generated by Django 3.0.3 on 2020-06-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0081_alter_organization_to_use_mdi_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='code_url',
            field=models.URLField(blank=True, default='', max_length=255),
        ),
    ]