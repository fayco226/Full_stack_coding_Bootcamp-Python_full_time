# Generated by Django 4.1.2 on 2023-01-04 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='name',
            new_name='nameF',
        ),
        migrations.RenameField(
            model_name='family',
            old_name='name',
            new_name='nameA',
        ),
    ]
