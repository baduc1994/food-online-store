# Generated by Django 4.1 on 2023-07-17 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('davur', '0035_demodate_demoorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demoorder',
            name='demo',
        ),
        migrations.DeleteModel(
            name='DemoDate',
        ),
        migrations.DeleteModel(
            name='DemoOrder',
        ),
    ]
