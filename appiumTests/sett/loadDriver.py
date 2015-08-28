from appium import webdriver
from sett import settings


class LoadDriver(object):

    @staticmethod
    def loadAppiumDriver():

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = 'Android Emulator'
        # Since the app is already installed launching it using package and activity name
        desired_caps['app'] = r'F:\automaty\atpwta.live.apk'
        desired_caps['appPackage'] = 'atpwta.live'
        desired_caps['appActivity'] = '.activity.Main'
        # Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
        desired_caps['appWaitActivity'] = '.activity.root.TournamentList'
        return webdriver.Remote(settings.appiumHub2, desired_caps)
