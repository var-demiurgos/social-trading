# Generated by Django 2.2.3 on 2019-08-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0005_auto_20190823_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade_list',
            name='lot',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trade_list',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trade_list',
            name='stoploss',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trade_list',
            name='takeprofit',
            field=models.FloatField(),
        ),
    ]
