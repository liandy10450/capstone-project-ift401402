# Generated by Django 3.0 on 2020-04-03 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JIT', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hazard',
            name='hazard_rating',
        ),
        migrations.AddField(
            model_name='bin',
            name='hazard_rating',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='hazard_rating',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
