# Generated by Django 4.1.7 on 2023-03-02 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_customer_store_custo_first_n_a7e990_idx_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='customer',
            name='store_custo_first_n_a7e990_idx',
        ),
        migrations.AlterModelTable(
            name='customer',
            table=None,
        ),
    ]
