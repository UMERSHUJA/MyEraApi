# Generated by Django 3.1.2 on 2020-10-14 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0005_auto_20201014_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
