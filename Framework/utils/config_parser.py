import configparser
import os


def get_config_value(section, key):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "configs", "config.ini"))
    return config.get(section, key)
