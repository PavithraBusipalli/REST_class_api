# Generated by Django 5.0.3 on 2024-03-04 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('PrdctCat_id', models.IntegerField(primary_key=True, serialize=False)),
                ('PrdctCat_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prdct_name', models.CharField(max_length=10)),
                ('Prdct_id', models.IntegerField()),
                ('Prdct_price', models.IntegerField()),
                ('Prdct_brand', models.CharField(max_length=10)),
                ('PrdctCat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productcategory')),
            ],
        ),
    ]