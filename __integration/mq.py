from hardware.mock_hardware import MockHardware
from networks.mq import MQ
from scheduler.scheduler import Scheduler
from dispatcher.dispatcher import Dispatcher
from configuration.load import load_config
from runner.run import run

config = load_config('./config.local.cfg')

run(
    debug=True,
    config=config,
    Hardware=MockHardware,
    Network=MQ,
    Dispatcher=Dispatcher,
    Scheduler=Scheduler,
    frequency=1
)
