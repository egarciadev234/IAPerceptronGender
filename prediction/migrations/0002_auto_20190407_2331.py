# Generated by Django 2.1.7 on 2019-04-07 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='height',
            field=models.IntegerField(null=True),
        ),
    ]