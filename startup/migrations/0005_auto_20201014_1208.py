# Generated by Django 3.1.2 on 2020-10-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0004_auto_20201014_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]