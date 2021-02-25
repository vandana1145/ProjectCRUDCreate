# Generated by Django 3.1.6 on 2021-02-17 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCRUDCreate', '0002_auto_20210202_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='fname',
            field=models.CharField(max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_num',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='subject',
            field=models.TextField(),
        ),
    ]
