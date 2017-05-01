import time
from hardware.mock_hardware import MockHardware
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
with MockHardware(
    red_pin=RED_PIN,
    green_pin=GREEN_PIN,
    blue_pin=BLUE_PIN,
    motor_pin=MOTOR_PIN,
    debug=True
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
        time.sleep(1)
