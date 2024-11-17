import pika
import json
from django.conf import settings
from .models import Payment

# RabbitMQ connection settings
rabbitmq_host = settings.RABBITMQ_HOST  # E.g., 'localhost'
queue_name = settings.RABBITMQ_QUEUE  # E.g., 'stripe_payments'


# Connect to RabbitMQ
def connect_to_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    return channel


# Callback to handle incoming messages from RabbitMQ
def callback(ch, method, properties, body):
    str_body = body.decode('utf-8')

    message = json.loads(str_body.replace("'", '"'))

    print(f"Received message: {message}")

    # Process the message (e.g., save to the database)
    try:
        # Create or update the Payment entry
        payment = Payment.objects.create(
            status=message['status'],
            payment_method=message['payment_method'],
            transaction_id=message['transaction_id'],
            amount=message['amount'],
            payment_date=message['date'],
        )
        print(f"Payment recorded: {payment}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Error processing message: {str(e)}")


# Start consuming messages
def start_consuming():
    channel = connect_to_rabbitmq()
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
