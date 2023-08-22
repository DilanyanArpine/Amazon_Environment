from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from common_.utilitis_.coustomLogger import *

class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    # def _find_element(self, locator):
    #     try:
    #         element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    #         return element
    #     except:
    #         print("ERROR: Element not found")
    #         exit(1)
    def _find_element(self,locator):

        if self._is_element_visible(locator):
            element = self.driver.find_element(*locator)
            return element
        else:
            print("ERROR: Element not found")
            exit(1)

    def _is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def _element_should_be_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except:
            print("ERROR: Element not visible but should be")

    def _get_title(self):
        return self.driver.title

    def _fill_field(self, element, text):
        element.clear()
        element.send_keys(text)

    def _mouse_move(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def _click_to_element(self, webElement):
        webElement.click()

    def _drag_and_drop(self):
        pass

    def _press_and_hold(self):
        pass

    def _get_element_text(self, webElement):
        return webElement.text

    def _get_element_text_by_locator(self, locator):
        element = self._find_element(locator)
        return element.text

    def _double_click(self):
        pass
