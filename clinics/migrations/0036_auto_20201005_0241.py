# Generated by Django 3.1.1 on 2020-10-05 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0035_auto_20201005_0238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='user',
        ),
        migrations.AddField(
            model_name='apply',
            name='name',
            field=models.CharField(default=1, max_length=50, verbose_name=': الاسم'),
            preserve_default=False,
        ),
    ]
