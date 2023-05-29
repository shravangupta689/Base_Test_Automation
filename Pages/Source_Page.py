from Library import ConfigReader

class Source_Details():
    def __init__(self,obj):
        global driver
        driver = obj

    def enter_source_name(self,source_name):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("Source Details", "Source-Name")).send_keys(source_name)

    def enter_host_name(self,host_name):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("Source Details", "Host-Name")).send_keys(host_name)

    def enter_credentials(self,credentials):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("Source Details", "Credentials")).send_keys(credentials)

    def enter_password(self,passsword):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("Source Details", "Password")).send_keys(passsword)

    def upload_file(self,file_path):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("Source Details", "Upload-File")).send_keys(file_path)

    def click_next(self):
        driver.find_element('xpath', ConfigReader.fetchElementlocators("Source Details", "Next")).click()
