# Generated by Django 3.2.7 on 2021-09-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='password'),
        ),
    ]
