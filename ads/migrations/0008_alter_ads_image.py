# Generated by Django 4.2.4 on 2023-08-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_alter_ads_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='image',
            field=models.ImageField(upload_to='images/ads/'),
        ),
    ]
