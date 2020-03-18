# Generated by Django 3.0.3 on 2020-02-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0017_auto_20200228_0116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['culture_code']},
        ),
        migrations.RemoveField(
            model_name='language',
            name='name',
        ),
        migrations.AddField(
            model_name='language',
            name='culture_code',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='iso_name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]