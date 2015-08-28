__author__ = 'robert'

from pages.mobilelocators import *

class PageLoader(object):

    def __init__(self, driver):
        self._driver = driver

    def get_HomePage(self):
        return HomePage(self._driver)

    def get_RangingsPage(self):
        return RangingsPage(self._driver)

    def get_PlayerListPage(self):
        return PlayerListPage(self._driver)

    def get_CallendarPage(self):
        return Callendar(self._driver)

    def getText(self, obj):
        return obj.get_attribute('text')

    def findelement(self, obj, *loc):
        element = obj.find_element