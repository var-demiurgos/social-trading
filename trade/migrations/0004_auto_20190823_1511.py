# Generated by Django 2.2.3 on 2019-08-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20190823_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade_list',
            name='lot',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='trade_list',
            name='order_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='trade_list',
            name='price',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='trade_list',
            name='stoploss',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='trade_list',
            name='takeprofit',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='trade_list',
            name='ticket',
            field=models.CharField(max_length=20),
        ),
    ]
