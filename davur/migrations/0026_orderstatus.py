# Generated by Django 4.1 on 2023-07-16 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('davur', '0025_rename_cartitemonl_cartitemonline_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_placed', models.BooleanField(default=False)),
                ('in_transit', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='davur.orderonline')),
            ],
        ),
    ]
