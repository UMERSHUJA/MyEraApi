# Generated by Django 3.1.2 on 2020-10-12 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Register',
        ),
        migrations.RenameField(
            model_name='joblist',
            old_name='contact',
            new_name='register',
        ),
        migrations.RenameField(
            model_name='startup',
            old_name='contact',
            new_name='register',
        ),
    ]
