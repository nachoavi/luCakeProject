# Generated by Django 4.2.6 on 2023-10-14 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_ingredients_recipes'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientcontacts',
            name='phone',
            field=models.CharField(max_length=15, null='N/A'),
            preserve_default='N/A',
        ),
    ]