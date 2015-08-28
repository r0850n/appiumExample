
from selenium.webdriver.common.by import By
from pageobject_support import cacheable, callable_find_by as find_by, callable_find_by

from page_objects import PageObject,page_element

from appium import webdriver


class MobileATPWTAElements(object):

    Montreal = find_by(how=By.XPATH, using="//android.widget.LinearLayout[@resource-id='atpwta.live:id/TournamentListItemLayoutRoot']")
    MainMenu = find_by(how=By.XPATH, using="//android.widget.Spinner[@resource-id='atpwta.live:id/NavBarMainMenuSpinner']")
    singles = find_by(how=By.ID, using='atpwta.live:id/RankingsListItem')

    list_of_players = find_by(how=By.CLASS_NAME, using='android.widget.ListView')

    rows = callable_find_by(how=By.CLASS_NAME, using='android.widget.TableRow', multiple=True)

    PLAYERS = callable_find_by(how=By.CLASS_NAME, using='android.widget.LinearLayout', multiple=True)

    #rankings = find_by(how=By.A , using='new UiSelector().text("Rankings")')

    def __init__(self, driver):
        self._driver = driver

    def _getrankingselement(self,_text):
        element = self._driver.find_element_by_android_uiautomator('new UiSelector().text("'+_text+'")')
        return element
    def _get_uiselectorBytext(self,_text):
        element = self._driver.find_element_by_android_uiautomator('new UiSelector().text("'+_text+'")')
        parent_elem=element.find_element_by_xpath('..')
        return parent_elem


class HomePage(object):

    NAV_BAR = find_by(how=By.ID, using='atpwta.live:id/NavBarMainMenuSpinner')
    CINCINATY = find_by(how=By.ID,using='atpwta.live:id/TournamentListItemLayoutRoot')

    #options
    TOP_BAR_OPTIONS = callable_find_by(how=By.CLASS_NAME, using='android.widget.LinearLayout', multiple=True)

    def __init__(self, driver):
        self._driver = driver


class RangingsPage(object):

    ATP_SINGLES = find_by(how=By.ID, using='atpwta.live:id/RankingsListItem')
    __ATP_RANKINGS = callable_find_by(how=By.XPATH, using='//android.widget.ListView/android.widget.LinearLayout/'
                                                       'android.widget.TextView', multiple=True)

    def __init__(self, driver):
        self._driver = driver

    @property
    def getAtRankings(self):
        return self.__ATP_RANKINGS


class PlayerListPage(object):

    list_of_players = find_by(how=By.CLASS_NAME, using='android.widget.ListView')
    PLAYERS = callable_find_by(how=By.CLASS_NAME, using='android.widget.LinearLayout', multiple=True)
    rows = callable_find_by(how=By.XPATH, using='//android.widget.TableRow/android.widget.TextView', multiple=True)

    def __init__(self, driver):
        self._driver = driver

    def get_players(self):
        return self.__PLAYERS


    def set_players(self, value):
        self.__PLAYERS = value


    def del_players(self):
        del self.__PLAYERS

    PLAYERS = property(get_players, set_players, del_players, "PLAYERS's docstring")


class Callendar(object):

    CITIES = callable_find_by(how=By.ID, using='atpwta.live:id/CalNameTextView', multiple=True)

    def __init__(self, driver):
        self._driver = driver

