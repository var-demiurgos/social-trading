# Generated by Django 2.2.3 on 2019-08-23 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0007_auto_20190823_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade_list',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True),
        ),
    ]
