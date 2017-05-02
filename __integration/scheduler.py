from hardware.mock_hardware import MockHardware
from networks.mock_network import MockNetwork
from scheduler.scheduler import Scheduler
from dispatcher.dispatcher import Dispatcher
from configuration.load import load_config
from runner.run import run

config = load_config()

run(
    debug=True,
    config=config,
    Hardware=MockHardware,
    Network=MockNetwork,
    Dispatcher=Dispatcher,
    Scheduler=Scheduler,
    frequency=1
)
