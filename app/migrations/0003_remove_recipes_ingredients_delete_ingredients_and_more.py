# Generated by Django 4.2.7 on 2023-11-06 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_usercollaborator_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='ingredients',
        ),
        migrations.DeleteModel(
            name='Ingredients',
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingredients',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]