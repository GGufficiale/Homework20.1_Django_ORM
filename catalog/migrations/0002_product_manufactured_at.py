# Generated by Django 5.0.7 on 2024-07-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateField(blank=True, null=True, verbose_name='дата производства продукта'),
        ),
    ]
