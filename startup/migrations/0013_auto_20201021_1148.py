# Generated by Django 3.1.2 on 2020-10-21 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0012_auto_20201021_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
