# Generated by Django 5.0.4 on 2024-05-04 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depositories', '0003_alter_depository_name'),
        ('events', '0003_remove_event_books_eventbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='related_depositiry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='depositories.depository'),
        ),
    ]