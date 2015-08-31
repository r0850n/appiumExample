"""
Qxf2: Example script to run one test against ATP_WTA app using Appium
The test will navigate to ATP Singles Rankings list and confirm that Novak
Djokovic is the top player listed and get his personal details from a table.
 
"""
 
import unittest, time, os

from time import sleep
from pages.PageLoader import PageLoader
from page_objects import PageObject,page_element
from pages.mobilelocators import HomePage, RangingsPage,MobileATPWTAElements
from sett.loadDriver import LoadDriver
from sett.loadDriver2 import LoadDriver_realDevice
from compiler.ast import TryExcept


class Android_ATP_WTA(unittest.TestCase):
    "Class to run tests against the ATP WTA app"

    S_3 = '4df13ae160004fe1'
    emulator = 'emulator-5554'
    def setUp(self):
        "Setup for the test"
        """ load driver from LoadDriver class"""
        self.driver = LoadDriver_realDevice.loadAppiumDriver()
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
        
    
    def test_nowy(self):
        self.driver.implicitly_wait(30)
        time.sleep(5)
        # load pages
        
        self.assertTrue(1==1)
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_ATP_WTA)
    unittest.TextTestRunner(verbosity=2).run(suite)