import time
from pages.element import BasePageElement
from pages.locators import MainPageLocators, LoginPageLocators
from sett.loadDriver import LoadDriver


class SearchTextElement(BasePageElement):
    locator = 'j_username'


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class LoginPage(BasePage):
    def login_as(self, username, password):
        username_input = self.driver.find_element(*LoginPageLocators.USER_NAME)
        password_input = self.driver.find_element(*LoginPageLocators.PASSWORD_AREA)
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

        username_input.send_keys(username)
        password_input.send_keys(password)
        self.driver.implicitly_wait(10)
        login_button.click()
        time.sleep(15)


class SearchResultsPage(BasePage):
    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
