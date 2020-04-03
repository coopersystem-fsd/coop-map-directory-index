# Generated by Django 3.0.3 on 2020-03-31 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0047_auto_20200327_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Niche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(blank=True, default='', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='tool',
            name='niches',
            field=models.ManyToManyField(to='mdi.Niche'),
        ),
    ]