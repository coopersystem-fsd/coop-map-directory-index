# Generated by Django 3.0.3 on 2020-03-22 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20200322_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='accounts.Role'),
            preserve_default=False,
        ),
    ]