# Generated by Django 2.1.4 on 2019-01-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorten',
            name='Xs_used',
            field=models.IntegerField(default=0),
        ),
    ]