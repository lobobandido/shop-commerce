# Generated by Django 3.2 on 2024-01-29 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('webshopcommerce', '0002_auto_20240129_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, upload_to='productos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='webshopcommerce.categoria')),
            ],
        ),
    ]
