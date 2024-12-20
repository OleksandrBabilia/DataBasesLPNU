# Generated by Django 5.0.4 on 2024-11-17 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_payment_date_payment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
        migrations.AddField(
            model_name='payment',
            name='success',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('stripe', 'Stripe'), ('paypal', 'PayPal')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
