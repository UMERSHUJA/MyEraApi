# Generated by Django 2.2 on 2020-10-07 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileManager',
        ),
    ]