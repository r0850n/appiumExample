from selenium.webdriver.common.by import By

from sett.pageobject_support import cacheable, callable_find_by as find_by
import pages.page


class MainPageLocators(object):
    GO_BUTTON = (By.ID, 'submit')


class LoginPageLocators(object):
    USER_NAME = (By.NAME, 'j_username')
    PASSWORD_AREA = (By.NAME, "j_password")
    LOGIN_BUTTON = (By.XPATH,  '//*[@id="submit"]')



class LoginPageL(object):
    USER_NAME = find_by(how=By.NAME, using='j_username')
    PASSWORD_AREA = find_by(how=By.NAME, using='j_password')
    LOGIN_BUTTON = find_by(how=By.XPATH,  using='//*[@id="submit"]')

    def __init__(self, driver):
        self._driver = driver

    def login(self, username, password):
       self.USER_NAME().send_keys(username)
       self.PASSWORD_AREA().send_keys(password)
       self.LOGIN_BUTTON().click()


    def _getpassword_area(self):
       return self.PASSWORD_AREA


class MobileATPWTAElements(object):

    MainMenu = find_by(how=By.XPATH, using="//android.widget.Spinner[@resource-id='atpwta.live:id/NavBarMainMenuSpinner']")

    def __init__(self, driver):
        self._driver = driver

class SearchResultsPageLocators(object):
    pass
