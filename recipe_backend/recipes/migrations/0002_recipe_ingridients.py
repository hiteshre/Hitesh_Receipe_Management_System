# Generated by Django 5.0.7 on 2024-08-23 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingridients',
            field=models.TextField(default='not available'),
            preserve_default=False,
        ),
    ]
