# Generated by Django 3.0.3 on 2020-04-04 03:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mdi', '0049_auto_20200331_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationsUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(max_length=32)),
                ('order', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdi.Organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "User's relationships to Organizations",
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='related_individuals',
            field=models.ManyToManyField(through='mdi.OrganizationsUsers', to=settings.AUTH_USER_MODEL),
        ),
    ]
