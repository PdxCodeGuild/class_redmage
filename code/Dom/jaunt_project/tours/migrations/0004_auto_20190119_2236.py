# Generated by Django 2.1.5 on 2019-01-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_auto_20190118_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='venue_size',
            field=models.CharField(max_length=20),
        ),
    ]
