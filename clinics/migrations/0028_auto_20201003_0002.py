# Generated by Django 3.1.1 on 2020-10-02 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0027_apply_apply_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinic',
            old_name='user',
            new_name='admin',
        ),
        migrations.AlterField(
            model_name='apply',
            name='ssid',
            field=models.ImageField(upload_to='apply', verbose_name='صوره البطاقه'),
        ),
    ]
