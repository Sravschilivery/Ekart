# Generated by Django 4.2.5 on 2023-10-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0002_alter_product_cat_alter_product_is_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Mobile'), (2, 'Shoes'), (3, 'Clothes')], verbose_name='Category'),
        ),
    ]