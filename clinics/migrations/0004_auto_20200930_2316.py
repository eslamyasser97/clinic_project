# Generated by Django 3.1.1 on 2020-09-30 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0003_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('male', 'ذكر'), ('female', 'انثي')], max_length=10, verbose_name=': النوع'),
        ),
    ]