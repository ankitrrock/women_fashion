# Generated by Django 3.0.6 on 2020-05-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sub_Item_type', models.CharField(max_length=20)),
            ],
        ),
    ]