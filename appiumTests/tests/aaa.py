import os
from pages.page import MainPage, LoginPage

__author__ = 'robert'
import unittest
from selenium import webdriver
from sett.loadDriver import LoadDriver
from pages.locators import LoginPageLocators, LoginPageL
from pages.glo import GlobalMethots
import pages.glo


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = LoadDriver().loadAppiumDriver()
        self.driver.get("http://tst.env.gociety.com")

    def test_search_in_python_org(self):
       log=LoginPageL(self.driver)
       #log._getusername().send_keys("aaa")
        #lp= LoginPage(self.driver)
       # lp.login_as("robert+1@gociety.com","tajne123")
      # log._getpassword_area().send_keys("bbb")
       log.login("aa","aaa")


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
