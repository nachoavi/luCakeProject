# Generated by Django 4.2.6 on 2023-10-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('saleDate', models.DateTimeField(auto_now_add=True)),
                ('subtotal', models.PositiveIntegerField()),
                ('iva', models.PositiveBigIntegerField()),
                ('total', models.PositiveIntegerField()),
            ],
        ),
    ]