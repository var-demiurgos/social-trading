# Generated by Django 2.2.3 on 2019-08-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0004_auto_20190823_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade_list',
            name='lot',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='trade_list',
            name='order_type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trade_list',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='trade_list',
            name='stoploss',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='trade_list',
            name='takeprofit',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='trade_list',
            name='ticket',
            field=models.IntegerField(),
        ),
    ]
