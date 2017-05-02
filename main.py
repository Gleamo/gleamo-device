from hardware.hardware import Hardware
from networks.mq import MQ
from scheduler.scheduler import Scheduler
from dispatcher.dispatcher import Dispatcher
from configuration.load import load_config
from runner.run import run

config = load_config('./config.cfg')

run(
    config=config,
    Hardware=Hardware,
    Network=MQ,
    Dispatcher=Dispatcher,
    Scheduler=Scheduler
)
