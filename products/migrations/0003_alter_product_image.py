# Generated by Django 4.2.7 on 2023-11-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_category_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]