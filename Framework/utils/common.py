import configparser
import os

# Defining the path to the configuration file
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "..", "configs", "config.ini")

# Create a configparser object
config_parser = configparser.ConfigParser()

# Read the configuration file
config_parser.read(CONFIG_FILE)


def get_config_value(section, key):
    """
    this function returns the value of the specified key from the specified section of the configuration file
    :param section:
    :param key:
    :return:
    """
    try:
        value = config_parser.get(section, key)
    except configparser.NoSectionError:
        print(f"Error: Section '{section}' not found")
        return None
    except configparser.NoOptionError:
        print(f"Error: Key '{key}' not found in the '{section}' of the configuration file")
        return None
    else:
        return value


