import sys
import logging
import configparser
import os

config_version = '1.0'


def create(config):
    logging.info("Config File angelegt")
    config['DEFAULT'] = {
        'config_version': config_version,
        # Deaktivierbare Teile
    }

    with open('config/config.ini', 'w') as configfile:
        config.write(configfile)


def config():
    try:
        # Config Datei anlegen und auslesen
        config = configparser.ConfigParser()
        if os.path.isfile("config/config.ini"):
            ("Config File gefunden")
            config.read('config/config.ini')
            conf = config['DEFAULT']
            if conf['config_version'] != config_version:
                os.remove("config/config.ini")
                logging.info("Config gelöscht")
                create(config)
            else:
                logging.info("Config Version ok")
        else:
            create(config)

        config.read('config/config.ini')
        conf = config['DEFAULT']
    except:
        print("Unexpected error Config anlegen Database.py:" + str(sys.exc_info()))
        logging.error(
            "Unexpected error Config anlegen Database.py:" + str(sys.exc_info()))
