# Generated by Django 3.1.1 on 2020-10-01 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0009_auto_20201001_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='user',
        ),
    ]
