# Generated by Django 3.0.6 on 2020-05-07 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmart', '0005_auto_20200507_0215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_category',
            name='product',
        ),
        migrations.AddField(
            model_name='add_product',
            name='size',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='add_product',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='add_product',
            name='sub_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Sub_Category',
        ),
    ]
