# Generated by Django 3.0.3 on 2020-03-20 19:40

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20200320_1940'),
        ('mdi', '0032_auto_20200319_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='admin_email',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mdi.Category'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='organization',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='lng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='sectors',
            field=models.ManyToManyField(blank=True, null=True, to='mdi.Sector'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Source'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mdi.Type'),
        ),
    ]
