# Generated by Django 4.1 on 2023-07-16 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('davur', '0030_rename_review_product_review_review_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='davur.product'),
        ),
    ]