from Library import ConfigReader

class General_Details():
    def __init__(self,obj):
        global driver
        driver = obj

    def enter_project_name(self,project_name):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("General Details", "Project-Name")).send_keys(project_name)

    def enter_project_description(self,description):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("General Details", "Description")).send_keys(description)

    def discovery_checkbox(self):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("General Details", "Manual-Checkbox")).click()

    def click_next(self):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("General Details", "Next")).click()
