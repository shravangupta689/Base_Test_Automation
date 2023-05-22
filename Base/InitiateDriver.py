#This script will setup and initiate the browser.

from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
import time
from Library import ConfigReader

def startbrowser():
    global driver
    path="./Driver/chromedriver.exe"
    driver= Chrome(executable_path=path)
    driver.get(ConfigReader.readConfigData('Details','Application_URL'))
    # driver.get(ConfigReader.readConfigData('Details', 'Application_URL1'))
    driver.maximize_window()
    time.sleep(5)
    return  driver

def closerBrowser():
    driver.close()