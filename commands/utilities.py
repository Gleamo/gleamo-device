import inspect
from .command import Command
from colors.color import Color
from buzzer.buzzer_pattern import BuzzerPattern

def create_buzzer(options):
    args = {}

    arguments = inspect.getfullargspec(BuzzerPattern.__init__)

    for arg in arguments[0]:
        if arg in options:
            args[arg] = options[arg]

    return BuzzerPattern(**args)

def convert_special_args(type, value):
    if type == 'color':
        return Color(r=value['r'], g=value['g'], b=value['b'])
    elif type == 'buzzer_pattern':
        if isinstance(value, str):
            options = {
                'none': BuzzerPattern.NONE,
                'short': BuzzerPattern.SHORT,
                'long': BuzzerPattern.LONG
            }
            return options[value]
        else:
            return create_buzzer(value)

def json_command_to_command(json):
    args = {}

    arguments = inspect.getfullargspec(Command.__init__)

    # Special Arugments
    special_args = ['color', 'buzzer_pattern']

    for arg in arguments[0]:
        if arg in json:
            if arg in special_args:
                args[arg] = convert_special_args(arg, json[arg])
            else:
                args[arg] = json[arg]

    return Command(**args)

def json_to_commands(json):
    if json == None or not 'commands' in json:
        return None

    commands = []

    for command_json in json['commands']:
        commands.append(json_command_to_command(command_json))

    return commands
