from hardware import Hardware
from polling import Polling
from scheduler import Scheduler
import time

#################
# Start up Gleamo
#################

ENDPOINT = 'http://api.gleamo.com/v1/'

RED_PIN = 14
GREEN_PIN = 15
BLUE_PIN = 18

MOTOR_PIN = 23

# Setup the services
with Hardware(
    red_pin=RED_PIN,
    green_pin=GREEN_PIN,
    blue_pin=BLUE_PIN,
    motor_pin=MOTOR_PIN
) as hardware:
    polling = Polling(ENDPOINT)

    scheduler = Scheduler(
      hardware_service=hardware,
      polling_service=polling
    )

    while true
        scheduler.run()
        # Heads up, sleep is in seconds wtf
        time.sleep(1)
