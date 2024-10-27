# Generated by Django 5.1.1 on 2024-10-01 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Srinu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('mobile_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=150)),
                ('dateofbirth', models.DateField()),
            ],
        ),
    ]
