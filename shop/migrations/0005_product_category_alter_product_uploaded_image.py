# Generated by Django 4.1.3 on 2025-04-18 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_uploaded_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='uploaded_image',
            field=models.FileField(blank=True, upload_to='uploads2/'),
        ),
    ]
