from Library import ConfigReader

class Destination_Details():
    def __init__(self,obj):
        global driver
        driver = obj

    def enter_target_name(self,target_name):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("Destination Details", "Target-Name")).send_keys(target_name)

    def enter_target_host(self,target_host_name):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("Destination Details", "Target-Host-Name")).send_keys(target_host_name)

    def enter_target_username(self,target_username):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("Destination Details", "Target-Username")).send_keys(target_username)

    def enter_target_password(self,target_password):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("Destination Details", "Target-Password")).send_keys(target_password)

    def click_create(self):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("Destination Details", "Create")).click()
