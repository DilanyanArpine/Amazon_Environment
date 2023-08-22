from selenium import webdriver
from selenium.webdriver.common.by import By
from sources.basePage_ import BasePage


class CartPage(BasePage):
    def __init__(self,driver:webdriver.Chrome):
        super().__init__(driver)



    def delete_product_from_cart(self):
        pass
