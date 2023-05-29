import time
import pytest
from Base import InitiateDriver
from Library import ConfigReader
from Pages import Login_Page
from Pages import Dashboard
from Pages import General_Page
from Pages import Source_Page
from Pages import Destination_Page
from Pages import Discovery_Page
from Pages import Wave_Migration_Page

@pytest.fixture(scope="class")
def driver():
    driver = InitiateDriver.startbrowser()
    driver.implicitly_wait(2)
    driver.delete_all_cookies()
    yield driver
    driver.close()

class TestLogin:
    def test_TC001Login(self, driver):
        login = Login_Page.LoginClass(driver)
        username = ConfigReader.fecthdata('Login', 'Username')
        password = ConfigReader.fecthdata('Login', 'Password')
        login.enter_username(username)
        login.enter_password(password)
        login.sign_in_button()

    def test_TC001Dashboard(self, driver):
        dash = Dashboard.Dashboard_Page(driver)
        dash.create_project()
        dash.pre_requisite_popup()

    def test_TC001General_Page(self,driver):
        general_details = General_Page.General_Details(driver)

        proj_name = ConfigReader.fecthdata('General Details', 'Name')
        general_details.enter_project_name(proj_name)

        description = ConfigReader.fecthdata('General Details', 'Description')
        general_details.enter_project_description(description)

        general_details.discovery_checkbox()
        general_details.click_next()

    def test_TC001Source_Page(self,driver):
        source_details = Source_Page.Source_Details(driver)

        source_name = ConfigReader.fecthdata('Source Details', 'Source-Name')
        source_details.enter_source_name(source_name)

        host_name = ConfigReader.fecthdata('Source Details', 'Host-Name')
        source_details.enter_host_name(host_name)

        credentials = ConfigReader.fecthdata('Source Details', 'Source-Username')
        source_details.enter_credentials(credentials)

        password = ConfigReader.fecthdata('Source Details', 'Source-Password')
        source_details.enter_password(password)

        file_path = ConfigReader.fecthdata('Source Details', 'File-Path')
        source_details.upload_file(file_path)

        source_details.click_next()

    def test_TC001Destination_Page(self,driver):
        destination_details = Destination_Page.Destination_Details(driver)

        target_name = ConfigReader.fecthdata('Destination Details', 'Target-Name')
        destination_details.enter_target_name(target_name)

        target_host_name = ConfigReader.fecthdata('Destination Details', 'Target-Host-Name')
        destination_details.enter_target_host(target_host_name)

        target_username = ConfigReader.fecthdata('Destination Details', 'Target-Username')
        destination_details.enter_target_username(target_username)

        target_password = ConfigReader.fecthdata('Destination Details', 'Target-Password')
        destination_details.enter_target_password(target_password)

        destination_details.click_create()


    def test_TC001Discovery_Page(self,driver):
        discovery = Discovery_Page.Discovery(driver)
        discovery.click_initiate_discovery()
        discovery.click_pre_requisite_check()
        discovery.click_initiate_planning()
        discovery.click_create_wave()
        driver.implicitly_wait(20)


    def test_TC001Wave_Migration(self,driver):
        wave_migration = Wave_Migration_Page.Wave_Migraton(driver)
        name = ConfigReader.fecthdata('Wave Details', 'Wave Name')
        wave_migration.wave_name(name)
        wave_migration.click_create_wave()
        time.sleep(9999)

'''
@pytest.fixture()
def test_TC001Login():
   driver = InitiateDriver.startbrowser()
   driver.implicitly_wait(10)
   driver.delete_all_cookies()
   login = Login_Page.LoginClass(driver)
   username = ConfigReader.fecthdata('Login', 'Username')
   password = ConfigReader.fecthdata('Login', 'Password')
   login.enter_username(username)
   login.enter_password(password)
   login.sign_in_button()
   time.sleep(5)
   driver.close()
'''

'''driver.find_element('id','email-sign-in').send_keys('admin@hpe.com')
   driver.find_element('id','password-sign-in').send_keys('right.MIX')
   driver.find_element('xpath',"//button[contains(text(),'Sign In')]").click()
   time.sleep(5)
   driver.close()'''






