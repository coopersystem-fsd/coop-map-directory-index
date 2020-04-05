# Generated by Django 3.0.3 on 2020-04-04 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0050_auto_20200404_0337'),
        ('accounts', '0025_user_languages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.AlterField(
            model_name='user',
            name='languages',
            field=models.ManyToManyField(blank=True, null=True, to='mdi.Language'),
        ),
    ]
