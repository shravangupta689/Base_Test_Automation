from Library import ConfigReader
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class Discovery():
    def __init__(self,obj):
        global driver
        driver = obj

    def click_initiate_discovery(self):
        driver.find_element('xpath', ConfigReader.fetchElementlocators(
            "Discovery", "Initiate Discovery")).click()

    def click_pre_requisite_check(self):
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable(
            (By.XPATH,ConfigReader.fetchElementlocators("Discovery", "Pre-requisite Check")))).click()
    def click_initiate_planning(self):
        WebDriverWait(driver, 500).until(EC.element_to_be_clickable(
            (By.XPATH,ConfigReader.fetchElementlocators("Discovery", "Initiate Planning")))).click()

    def click_create_wave(self):
        WebDriverWait(driver, 500).until(EC.element_to_be_clickable(
            (By.XPATH, ConfigReader.fetchElementlocators("Discovery", "Create Wave")))).click()

