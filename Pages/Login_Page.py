
import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from Base import InitiateDriver
from Library import ConfigReader
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException


class LoginClass:

    def __init__(self,obj):
       global driver
       driver= object

    def enter_username(self, username):

        driver.find_element_by_id(ConfigReader.fetchElementlocators("Registration", "Username")).send_keys(username)

    def enter_password(self, password):

        driver.find_element_by_id(ConfigReader.fetchElementlocators("Registration", "Password")).send_keys(password)
        # driver.find_element('id','id_name')


    #def password(self, password):
