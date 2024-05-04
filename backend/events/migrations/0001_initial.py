# Generated by Django 5.0.4 on 2024-05-04 09:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0008_ganre_book_ganres'),
        ('depositories', '0003_alter_depository_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('SH', 'Shipment'), ('AR', 'Arrival'), ('CO', 'Checkout'), ('RT', 'Return'), ('AD', 'Addition')], max_length=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('books', models.ManyToManyField(related_name='events', to='books.book')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventDepository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='depositories.depository')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
            options={
                'unique_together': {('event', 'depository')},
            },
        ),
    ]
