#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port='32771'))
channel = connection.channel()

channel.queue_declare(queue='hello')
for item in range(10):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
    print(" [x] Sent 'Hello World!': " + str(item)
connection.close()
