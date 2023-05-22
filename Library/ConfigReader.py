import configparser


def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Config.cfg")
    return config.get(section, key)


def fetchElementlocators(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Elements.cfg")
    return config.get(section, key)

def fecthdata(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Data.cfg")
    return config.get(section, key)
