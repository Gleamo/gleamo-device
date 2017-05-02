import time

def run(Hardware, Network, Scheduler, Dispatcher, config, frequency=0.017, debug=False):
    with Hardware(
        red_pin=config['red_pin'],
        green_pin=config['green_pin'],
        blue_pin=config['blue_pin'],
        motor_pin=config['motor_pin'],
        debug=debug
    ) as hardware:
        network_service = Network(config['endpoint'], config['username'], config['password'])
        dispatcher = Dispatcher(
            hardware_service=hardware
        )

        scheduler = Scheduler(
          network_service=network_service,
          dispatcher_service=dispatcher
        )

        while True:
            scheduler.run()
            time.sleep(frequency)
