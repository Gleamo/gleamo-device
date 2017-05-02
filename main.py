import time
from hardware.hardware import Hardware
from networks.mq import MQ
from scheduler.scheduler import Scheduler
from dispatcher.dispatcher import Dispatcher

#################
# Start up Gleamo
#################

# XXX Load from configuration file
ENDPOINT = 'http://api.gleamo.com/v1/'
USERNAME = 'gleamo'
PASSWORD = 'gleamo'

RED_PIN = 14
GREEN_PIN = 15
BLUE_PIN = 18

MOTOR_PIN = 2

# Setup the services
with Hardware(
    red_pin=RED_PIN,
    green_pin=GREEN_PIN,
    blue_pin=BLUE_PIN,
    motor_pin=MOTOR_PIN
) as hardware:
    network_service = MQ(ENDPOINT, USERNAME, PASSWORD)
    dispatcher = Dispatcher(
        hardware_service=hardware
    )

    scheduler = Scheduler(
      network_service=network_service,
      dispatcher_service=dispatcher
    )

    while True:
        scheduler.run()
        time.sleep(0.017)
