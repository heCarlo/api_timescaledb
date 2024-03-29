# Generated by Django 5.0.3 on 2024-03-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('code', models.CharField(max_length=50)),
                ('direction', models.FloatField(max_length=50)),
                ('temperature', models.FloatField()),
                ('rh', models.FloatField()),
                ('pressure', models.FloatField()),
                ('precip', models.FloatField()),
                ('prmsl', models.FloatField()),
                ('tmpsrf', models.FloatField()),
                ('vel_gfs', models.FloatField()),
                ('vel_twr', models.FloatField()),
            ],
        ),
    ]
