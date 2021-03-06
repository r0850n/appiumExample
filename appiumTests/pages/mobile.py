"""
Qxf2: Example script to run one test against ATP_WTA app using Appium
The test will navigate to ATP Singles Rankings list and confirm that Novak
Djokovic is the top player listed and get his personal details from a table.
 
"""
 
import unittest, time, os
from appium import webdriver
from time import sleep
from pages.PageLoader import PageLoader
from pages.mobilelocators import MobileATPWTAElements

class Android_ATP_WTA(unittest.TestCase):
    "Class to run tests against the ATP WTA app"

    S_3 = '4df13ae160004fe1'
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = self.S_3
        # Since the app is already installed launching it using package and activity name
        desired_caps['appPackage'] = 'atpwta.live'
        desired_caps['appActivity'] = '.activity.Main'
        # Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
        desired_caps['appWaitActivity'] = '.activity.root.TournamentList'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
 
    def test_atp_wta(self):
        "Testing the ATP WTA app "
        self.driver.implicitly_wait(30)
        time.sleep(5)


        # click on Navigation Bar MainMenu by finding element by xpath

       # menubar = self.driver.find_element_by_xpath("//android.widget.Spinner[@resource-id='atpwta.live:id/NavBarMainMenuSpinner']")
        mobile_elements = MobileATPWTAElements(self.driver)
       # montreal = mobile_elements._get_uiselectorBytext("Montreal")
       # print(montreal.get_attribute('text'))
        #montreal.click()
        menubar = mobile_elements.MainMenu()
        menubar.click()
 
        # From list of options available click on Rankings by finding element using uiautomator
       # rankings = self.driver.find_element_by_android_uiautomator('new UiSelector().text("More")')
        rankings = mobile_elements._getrankingselement("Rankings")
        rankings.click()
 
        # click on ATP Singles by finding element using id
       # singles = self.driver.find_element_by_id('atpwta.live:id/RankingsListItem')
        singles = mobile_elements.singles()
        singles.click()
 
        # Assert that Novak Djokovic is the top listed player
      #  elmnt = self.driver.find_element_by_id('atpwta.live:id/Player1TV')
       # self.assertEqual('Novak Djokovic', elmnt.get_attribute('text'))
      #  print (elmnt.get_attribute('text'))

        aaa = mobile_elements.list_of_players()
        cols = aaa.find_elements_by_class_name('android.widget.LinearLayout')
        cols[0].click()

        #for i in range(0,len(aaa)):
        #   cols = aaa[i].find_elements_by_class_name('android.widget.LinearLayout')
         #  for j in range(0,len(cols)):
         #      playername=cols[j].find_elements_by_class_name('android.widget.TextView')
         #      for z in playername:
          #         print(z.get_attribute('text')+" -- ")



 
        #elmnt = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=0]")
        #elmnt.click()

 
        # Print the contents of Table listed for the top ranked player
        table = self.driver.find_element_by_android_uiautomator("new UiSelector().className(android.widget.TableLayout)")
        #rows = table.find_elements_by_class_name('android.widget.TableRow')
        rows = mobile_elements.rows()
        for i in range(0, len(rows)):
            cols = rows[i].find_elements_by_class_name('android.widget.TextView')
            for j in range(0, len(cols)):
                print(cols[j].get_attribute('text')+" -- "),
            print("")
 
 
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_ATP_WTA)
    unittest.TextTestRunner(verbosity=2).run(suite)