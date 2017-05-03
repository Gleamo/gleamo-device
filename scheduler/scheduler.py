from time import time
from networks.inetwork import INetwork
from dispatcher.dispatcher import Dispatcher
from commands.command import Command
from state.state import State
from colors.color import Color
from buzzer.buzzer_pattern import BuzzerPattern

DefaultCommand = Command(
    duration=1,
    color=Color.no_change(),
    buzzer_pattern=BuzzerPattern.NONE
)

class Scheduler:
    def __init__(self, dispatcher_service: Dispatcher, network_service: INetwork):
        self.dispatcher_service = dispatcher_service
        self.network_service = network_service

        self.commands = []
        self.commands.append(DefaultCommand)

        self.current_command = DefaultCommand

        self.state = State(Color(255, 255, 255), BuzzerPattern.NONE)
        self.last_run = time()
        self.last_poll = 0

    def update_commands(self, commands, now):
        # For now, we will just replace the current commands
        if commands != None:
            self.commands = commands
            self.current_command = self.commands[0]
            del self.commands[0]
            self.current_command.set_start_values(now, self.state.color)

    def get_current_command(self, now):
        if self.current_command.is_expired(now):
            # Make sure our state is up to date
            if not self.current_command.color.is_no_change():
                self.state = State(self.current_command.color, BuzzerPattern.NONE)

            if len(self.commands) > 0:
                self.current_command = self.commands[0]
                del self.commands[0]
                self.current_command.set_start_values(now, self.state.color)
            else:
                # We have no commands, use the default, but update the
                # start values
                self.current_command = DefaultCommand
                self.current_command.set_start_values(now, self.state.color)

        return self.current_command

    # determine which commands should get run
    def run_commands(self, now):
        current_command = self.get_current_command(now)

        if current_command != None:
            next_state = self.dispatcher_service.dispatch(current_command, now)
            self.state = next_state

    def run(self):
        now = time() * 1000

        if now - self.last_poll > self.network_service.get_poll_interval():
            self.last_poll = now
            self.update_commands(self.network_service.check(), now)

        self.last_run = now
        self.run_commands(now)
