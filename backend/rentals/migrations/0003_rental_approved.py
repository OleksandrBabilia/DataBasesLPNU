# Generated by Django 5.0.4 on 2024-11-15 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0002_alter_rental_rental_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
