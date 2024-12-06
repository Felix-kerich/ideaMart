# Generated by Django 5.1.3 on 2024-12-06 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_seller_account_delete_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_account',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=10),
        ),
    ]
