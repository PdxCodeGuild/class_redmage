# Generated by Django 2.1.5 on 2019-01-22 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_auto_20190122_0617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='region',
        ),
    ]