# Generated by Django 3.1.7 on 2021-02-25 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCRUDCreate', '0007_auto_20210225_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='lname',
            field=models.CharField(max_length=100, verbose_name='Last Name'),
        ),
    ]
