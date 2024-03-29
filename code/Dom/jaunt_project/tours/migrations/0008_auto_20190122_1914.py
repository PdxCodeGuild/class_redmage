# Generated by Django 2.1.5 on 2019-01-22 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_remove_venue_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='venue',
            name='state',
        ),
        migrations.AlterField(
            model_name='venue',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.City'),
        ),
    ]
