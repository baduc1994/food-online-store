# Generated by Django 4.1 on 2023-07-15 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('davur', '0021_cartonl_orderonl_nullitemonl_listorderonl_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='country',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='zip',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='mobile',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]
