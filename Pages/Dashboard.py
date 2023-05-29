from Library import ConfigReader

class Dashboard_Page():
    def __init__(self, obj):
        global driver
        driver = obj

    def create_project(self):
        driver.find_element('xpath',ConfigReader.fetchElementlocators("Dashboard", "Create-project")).click()

    def pre_requisite_popup(self):
        driver.find_element('xpath',ConfigReader.fetchElementlocators("Dashboard", "Pre-Requisite-Continue")).click()


