# Generated by Django 3.1.1 on 2020-09-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20200912_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]