from py.selenium.webdriver.support.wait import WebDriverWait

class GlobalMethots(object):

    def findElement(driver, obj):
        print('ciepie po : '+obj)
        element = driver.find_element(obj)
        return element
