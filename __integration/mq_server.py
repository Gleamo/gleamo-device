#!/usr/bin/env python
import pika
from configuration.load import load_config

config = load_config('./config.local.cfg')

credentials = pika.PlainCredentials(config['username'], config['password'])
connection = pika.BlockingConnection(pika.ConnectionParameters(host=config['endpoint'], credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='commands')

channel.basic_publish(
    exchange='',
    routing_key='commands',
    body='''
    {
        "commands": [
            {
                "duration": 1000,
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
