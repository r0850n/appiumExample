__author__ = 'robert'

import unittest, time, os
from appium import webdriver
from time import sleep
from pages.mobilelocators import MobileATPWTAElements

class Android_esky_app(unittest.TestCase):
    "Class to run tests against the ATP WTA app"

    S_3 = '4df13ae160004fe1'
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = self.S_3
        # Since the app is already installed launching it using package and activity name
        desired_caps['appPackage'] = 'com.esky'
        desired_caps['appActivity'] = '.app.MainActivity'
        # Adding appWait Activity since the activity name changes as the focus shifts to the Esky app's first page
       # desired_caps['appWaitActivity'] = 'com.esky'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_atp_esky(self):
        "Testing the Esky app "
        self.driver.implicitly_wait(30)
        time.sleep(5)

        print(str(self.driver.page_source))

#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_esky_app)
    unittest.TextTestRunner(verbosity=2).run(suite)
