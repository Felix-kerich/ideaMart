# Generated by Django 5.1.3 on 2024-12-05 22:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketplace', '0002_product_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_product', to='marketplace.product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mpesa_receipt_number', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Success', 'Success'), ('Failed', 'Failed'), ('Cancelled', 'Cancelled')], max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('transaction_date', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='marketplace.product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
