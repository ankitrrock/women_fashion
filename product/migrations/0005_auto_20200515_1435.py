# Generated by Django 3.0.6 on 2020-05-15 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200515_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
