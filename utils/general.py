from py.path import local
import os
import configparser

project_path = local(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

def get_config():
    config_file_Path = os.path.join(project_path, "./config.ini")
    config_parser = configparser.RawConfigParser()
    config_parser.read(config_file_Path)
    return config_parser

def get_setting(parent, key):
    config = get_config()
    return config.get(parent, key)