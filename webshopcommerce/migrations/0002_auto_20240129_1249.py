# Generated by Django 3.2 on 2024-01-29 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webshopcommerce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]