# Generated by Django 3.1.1 on 2020-10-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0026_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='apply_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
