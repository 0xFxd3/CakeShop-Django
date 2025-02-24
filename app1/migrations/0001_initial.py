# Generated by Django 4.2.5 on 2023-11-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('membership', models.IntegerField()),
            ],
        ),
    ]
