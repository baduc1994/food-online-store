# Generated by Django 4.1 on 2023-07-05 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('davur', '0003_alter_product_product_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='complete',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]