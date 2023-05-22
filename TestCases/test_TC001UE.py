import time
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from Base import InitiateDriver
from Library import ConfigReader
from selenium.webdriver.common.alert import Alert
from Pages import Login_Page
from Pages.Login_Page import LoginClass
from selenium.common.exceptions import NoSuchElementException


#@pytest.fixture()
def test_TC001Login():
   global driver
   driver = InitiateDriver.startbrowser()

   driver.implicitly_wait(10)
   driver.delete_all_cookies()


   #driver.find_element_by_id("email-sign-in").sendkeys("")

   driver.close()





