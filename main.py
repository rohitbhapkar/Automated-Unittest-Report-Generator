#------ AUTOMATED UNIT TEST REPORT GENERATOR-----
#------ CODE bY - ROHIT BHAPKAR---------

#importing libraries
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import HtmlTestRunner

# main class 
class GoogleSearchTest(unittest.TestCase):

    #setup base class
    def setUp(self):
        os.environ['PATH'] += r'C:\Users\Rohit Bhapkar\Desktop\Testing\Unittest project'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://www.google.com/')

    #test cases
    def test_case1(self):
        self.driver.find_element(By.NAME, 'q').send_keys("Automation Applications")
        self.driver.find_element(By.NAME, 'btnK').click()

    def test_case2(self):
        self.driver.find_element(By.NAME, 'q').send_keys("Automation Future Scope")
        self.driver.find_element(By.NAME, 'btnK').click()

    #teardown class
    def tearDown(self):
        self.driver.quit()
        print("Tests Completed")

# Main driver program with report Generator 
unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Rohit Bhapkar/Desktop/Testing/Unittest project')) 