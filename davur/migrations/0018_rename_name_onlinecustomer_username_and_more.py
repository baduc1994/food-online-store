# Generated by Django 4.1 on 2023-07-14 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('davur', '0017_onlinecustomer_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onlinecustomer',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='onlinecustomer',
            name='user',
        ),
        migrations.AddField(
            model_name='onlinecustomer',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='onlinecustomer',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
