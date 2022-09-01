from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Chrome():
    def __init__(self):
        driverlocation = r'C:\Users\computer world\.wdm\drivers\chromedriver\win32\104.0.5112\chromedriver.exe'
        #    loading chrome browser

        self.driver = webdriver.Chrome(driverlocation)

    def loginTC(self):
        try:
            self.driver.implicitly_wait(3)
            url = "http://www.demo.guru99.com/V4/"
            self.driver.get(url)
            userForm = self.driver.find_element(By.XPATH, "//input[@name='uid']")
            userForm.send_keys("mngr435500")
            pwForm = self.driver.find_element(By.XPATH, "//input[@name='password']")
            pwForm.send_keys("hurUvUh")
            loginButton = self.driver.find_element(By.XPATH, "//input[@value='LOGIN']")

            loginButton.click()
            time.sleep(2)

            addCustomer = self.driver.find_element("link text", 'New Customer')
            addCustomer.click()
            time.sleep(1)
            customerName = self.driver.find_element("name",'name')

            customerName.send_keys('SEPTONICS')
            time.sleep(1)
            customerDob = self.driver.find_element("name",'dob')
            customerDob.send_keys('25-08-2022')
            time.sleep(1)
            customerAddr = self.driver.find_element("name",'addr')
            customerAddr.send_keys('Chandigarh')
            time.sleep(1)
            customerCity = self.driver.find_element("name",'city')
            customerCity.send_keys('Chandigarh')
            time.sleep(1)
            customerState = self.driver.find_element("name",'state')
            customerState.send_keys('Punjab')
            time.sleep(1)
            customerPin = self.driver.find_element("name",'pinno')
            customerPin.send_keys('133301')
            time.sleep(1)
            customerPhone = self.driver.find_element("name",'telephoneno')
            customerPhone.send_keys('9536453258')
            time.sleep(1)
            customerEmail = self.driver.find_element("name",'emailid')
            customerEmail.send_keys('rs09798087@gmail.com')
            time.sleep(1)
            customerPass = self.driver.find_element("name",'password')
            customerPass.send_keys('2345')
            time.sleep(1)
            customerSub = self.driver.find_element("name",'sub')
            customerSub.click()
            time.sleep(1)
            customerDelete = self.driver.find_element("link text", 'Delete Customer')
            customerDelete.click()
            time.sleep(1)
            customerID = self.driver.find_element("name",'cusid')
            customerID.send_keys('59610')
            time.sleep(1)
            customerSub = self.driver.find_element("name",'AccSubmit')
            customerSub.click()
            print("Logged in")
            # self.driver.quit()

        except Exception as errorMessage:
            print("This is the error: " + str(errorMessage))


chromeBrowser = Chrome()
chromeBrowser.loginTC()