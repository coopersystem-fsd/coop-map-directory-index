# Generated by Django 3.0.3 on 2020-04-06 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersocialnetwork',
            name='identifier',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
