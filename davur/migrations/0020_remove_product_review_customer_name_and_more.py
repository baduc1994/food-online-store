# Generated by Django 4.1 on 2023-07-15 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('davur', '0019_democustomer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_review',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='product_review',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='DemoCustomer',
        ),
        migrations.DeleteModel(
            name='OnlineCustomer',
        ),
    ]