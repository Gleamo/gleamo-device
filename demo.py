import time
from hardware.hardware import Hardware
from networks.mock_network import MockNetwork
from scheduler.scheduler import Scheduler
from dispatcher.dispatcher import Dispatcher

#################
# Start up Gleamo
#################

ENDPOINT = 'http://api.gleamo.com/v1/'

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
    mock_network = MockNetwork(ENDPOINT)
    dispatcher = Dispatcher(
        hardware_service=hardware
    )

    scheduler = Scheduler(
      network_service=mock_network,
      dispatcher_service=dispatcher
    )

    while True:
        scheduler.run()
        # Heads up, sleep is in seconds wtf
        # XXX When there are commands in the queue, run at 0.1,
        # when there are no commands in the queue, back off to 5 seconds
        time.sleep(1)
