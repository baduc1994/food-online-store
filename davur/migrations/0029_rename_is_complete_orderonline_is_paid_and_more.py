# Generated by Django 4.1 on 2023-07-16 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('davur', '0028_remove_orderstatus_customer_remove_orderstatus_order_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderonline',
            old_name='is_complete',
            new_name='is_paid',
        ),
        migrations.AlterField(
            model_name='orderonline',
            name='order_status',
            field=models.CharField(choices=[('Order Placed', 'Order Placed'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered'), ('Completed', 'Completed')], default=4, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='OrderStatus',
        ),
    ]
