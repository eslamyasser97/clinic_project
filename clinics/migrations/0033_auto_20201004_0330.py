# Generated by Django 3.1.1 on 2020-10-04 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0032_auto_20201004_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='works_hour',
            field=models.IntegerField(verbose_name=': ساعات العمل اليوميه'),
        ),
    ]
