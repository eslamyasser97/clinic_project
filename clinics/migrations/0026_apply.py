# Generated by Django 3.1.1 on 2020-10-02 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0025_auto_20201002_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name=': الاسم')),
                ('telephone', models.CharField(blank=True, max_length=50, null=True, verbose_name=': التليفون:')),
                ('ssid', models.FileField(upload_to='apply', verbose_name='صوره البطاقه')),
                ('comment', models.CharField(max_length=2000, verbose_name='التعليق')),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_clinic', to='clinics.clinic')),
            ],
        ),
    ]