from configparser import RawConfigParser, NoSectionError

def load_config(path='./config.cfg'):
    config = RawConfigParser()
    config.read(path)

    configDict = {}

    try:
        configDict['endpoint'] = config.get('mq', 'endpoint')
        configDict['username'] = config.get('mq', 'username')
        configDict['password'] = config.get('mq', 'password')
        configDict['red_pin'] = config.getint('pins', 'red_pin')
        configDict['green_pin'] = config.getint('pins', 'green_pin')
        configDict['blue_pin'] = config.getint('pins', 'blue_pin')
        configDict['motor_pin'] = config.getint('pins', 'motor_pin')
    except NoSectionError:
        print('Invalid config. Make sure to copy the config.example.cfg to %s' % path)
        exit()

    return configDict
