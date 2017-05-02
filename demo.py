from hardware.hardware import Hardware
from networks.mock_network import MockNetwork
from scheduler.scheduler import Scheduler
from dispatcher.dispatcher import Dispatcher
from configuration.load import load_config
from runner.run import run

config = load_config('./config.cfg')

run(
    config=config,
    Hardware=Hardware,
    Network=MockNetwork,
    Dispatcher=Dispatcher,
    Scheduler=Scheduler
)
