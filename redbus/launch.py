
from selenium import webdriver
import time
class InputFormsCheck():
    def setUp(self):
        self.driver=webdriver.Chrome("C:\\Users\\CSC\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.redbus.in/")
        self.driver.maximize_window()
        li=self.driver.find_element_by_xpath("//div[@id='manageHeaderdd']").click()
        ma=self.driver.find_elements_by_xpath("//div[@id='hmb']")
        for i in ma:
            print(i.text)

s=InputFormsCheck()

