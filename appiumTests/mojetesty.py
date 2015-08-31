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

    def test_robert(self):
        "Testing the ATP WTA app "
        self.driver.implicitly_wait(30)
        time.sleep(5)

        # init page loader
        pageLoader = PageLoader(self.driver)

        # click on Navigation Bar MainMenu by finding element by xpath
        # load mobile locators

        mobile_elements = pageLoader.get_HomePage()
        rangingsPage = pageLoader.get_RangingsPage()
        playerListPage = pageLoader.get_PlayerListPage()

        menubar = mobile_elements.NAV_BAR()
        menubar.click()
 
        # From list of options available click on Rankings by finding element using uiautomator
        rankings = mobile_elements.TOP_BAR_OPTIONS()
        rankings[3].click()
        for rank in rangingsPage.getAtRankings():
            print(pageLoader.getText(rank))

        print(rangingsPage.getAtRankings()[0].text+" wawalilo to /n")
        rangingsPage.getAtRankings()[0].click()
        time.sleep(5)

        player = pageLoader.get_PlayerListPage().list_of_players()
        lista_playerow = []

        aaa = player.find_elements_by_id('atpwta.live:id/Player1TV')
        lista_playerow.extend(aaa)

        for playerName in lista_playerow:
            print(pageLoader.getText(playerName))
        print("-------------------------------------------------------")
        time.sleep(5)
        #swipe DOWN        x1  y1  x2  y2   sleep
        #self.driver.swipe(475, 0, 475, 100, 400)
        time.sleep(5)
        #swipe UP
        #self.driver.swipe(475, 500, 475, 0, 400)
        time.sleep(5)
        lista_playerow.extend(aaa)
        for playerName in lista_playerow:
            print(pageLoader.getText(playerName))
        print("-------------------------------------------------------")

        
        aaa[0].click()

        rows = pageLoader.get_PlayerListPage().rows()
        for i in rows:
            print(pageLoader.getText(i)+" -- ")
        print("")
        
    
    def test_nowy(self):
        self.driver.implicitly_wait(30)
        time.sleep(5)
        # load pages
        pageLoader = PageLoader(self.driver)
        mobile_elements = pageLoader.get_HomePage()
        rangingsPage = pageLoader.get_RangingsPage()
        playerListPage = pageLoader.get_PlayerListPage()
        callendar = pageLoader.get_CallendarPage()

        menubar = mobile_elements.NAV_BAR()
        menubar.click()

        rankings = mobile_elements.TOP_BAR_OPTIONS()
        rankings[2].click()

        for citiesName in callendar.CITIES():
            print(pageLoader.getText(citiesName))

        callendar.CITIES()[0].click()
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_ATP_WTA)
    unittest.TextTestRunner(verbosity=2).run(suite)