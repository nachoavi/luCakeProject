# Generated by Django 4.2.7 on 2023-11-03 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercollaborator',
            name='password',
            field=models.BinaryField(max_length=150),
        ),
    ]