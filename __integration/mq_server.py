#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('gleamo', 'gleamo')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='commands')

channel.basic_publish(
    exchange='',
    routing_key='commands',
    body='''
    {
        "commands": [
            {
                "duration": 5000,
                "start_offset": 0,
                "end_offset": 0,
                "color": {
                    "r": 100,
                    "g": 120,
                    "b": 250
                },
                "buzzer_pattern": "none"
            }
        ]
    }
    '''
)
print('[x] Sent Commands!')
connection.close()
