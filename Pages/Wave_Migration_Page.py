from Library import ConfigReader

class Wave_Migraton():
    def __init__(self,obj):
        global driver
        driver = obj

    def wave_name(self,name):
        driver.find_element('xpath', ConfigReader.fetchElementlocators(
            "Wave Plan", "Wave Name")).send_keys(name)

    def click_create_wave(self):
        driver.find_element('xpath', ConfigReader.fetchElementlocators(
            "Wave Plan", "Create-button")).click()

    def select_vm_name(self,vmname):
        driver.find_element('xpath', ConfigReader.fetchElementlocators(
            "Wave Plan", "VMName")).send_keys(vmname)

    def select_vm_network(self,vmnetwork):
        driver.find_element('xpath', ConfigReader.fetchElementlocators(
            "Wave Plan", "VMnetwork")).send_keys(vmnetwork)
