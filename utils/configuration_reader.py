import json


def read_config():

    try:
        with open("config.json", "r") as file:
            config_data = json.load(file)
        return config_data
    except:
        with open("../config.json", "r") as file:
            config_data = json.load(file)
        return config_data


