from appium import webdriver
from sett import settings
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class LoadDriver(object):

    @staticmethod
    def loadAppiumDriver():

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = settings.emu
        # Since the app is already installed launching it using package and activity name
        #desired_caps['app'] = 'sauce-storage:atpwta.live.apk' 
        desired_caps['appPackage'] = 'atpwta.live'
        desired_caps['appActivity'] = '.activity.Main'
        # Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
        desired_caps['appWaitActivity'] = '.activity.root.TournamentList'
        return webdriver.Remote(settings.appiumHub2, desired_caps)
