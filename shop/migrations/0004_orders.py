# Generated by Django 5.0 on 2024-01-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact_alter_product_desc_alter_product_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=17)),
                ('email', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=90)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=90)),
            ],
        ),
    ]
