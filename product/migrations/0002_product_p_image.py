# Generated by Django 3.0.6 on 2020-05-12 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='p_image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]
