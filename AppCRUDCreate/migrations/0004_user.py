# Generated by Django 3.1.6 on 2021-02-18 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCRUDCreate', '0003_auto_20210217_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='User Name')),
                ('firstname', models.CharField(max_length=100, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=1000)),
                ('date_joined', models.DateField()),
            ],
        ),
    ]
