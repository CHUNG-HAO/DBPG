# Generated by Django 5.0.6 on 2024-06-18 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStart', '0004_remove_option_dealerid_option_supplierid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='SupplierID',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='appStart.supplier'),
        ),
    ]