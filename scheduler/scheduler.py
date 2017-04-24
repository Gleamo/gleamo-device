from hardware import Hardware
from polling import Polling
from time import time
from commands import DefaultCommand, Command

class Scheduler:
    def __init__(self, hardware_service: Hardware, polling_service: Polling):
        self.hardware_service = hardware_service
        self.polling_service = polling_service
        self.commands = DefaultCommand

        polling_service.set_scheduler(self)

    def update_commands(self, commands):
        # For now, we will just replace the current commands
        if commands != null:
            self.commands = commands
            self.current_command = self.commands.pop()

    def get_current_command(self, now):
        if current_command.is_expired(now):
            if len(self.current_command) > 0:
                self.current_command = self.commands.pop()
            else:
                self.current_command = DefaultCommand

        return self.current_command

    # determine which commands should get run
    def run_commands(self, now, diff):
        current_command = self.get_current_command(now)
        # XXX
        # send the command to the exector with the hardware service and command
        # and the state
        # It will return the next state, which we store

    def run(self):
        now = time()
        diff = now - self.last_run
        self.last_run = now

        if now - last_poll > self.polling_service.get_poll_interval():
            self.update_commands(self.polling_service.check())

        self.run_commands(now, diff)
