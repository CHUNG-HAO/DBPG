# Generated by Django 5.0.6 on 2024-06-18 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appStart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='DaelerID',
            new_name='DealerID',
        ),
    ]
