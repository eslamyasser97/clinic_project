# Generated by Django 3.1.1 on 2020-10-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201009_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='profile', verbose_name=': الصوره البطاقه الشخصيه'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type_of_person',
            field=models.CharField(choices=[('Male', 'ذكر'), ('Female', 'انثي')], max_length=8, verbose_name='النوع'),
        ),
    ]
