from selenium.webdriver.common.by import By

# from Baseclass import Baseclass
from Pageobject.ShopPage import ShopPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.XPATH, "//div[@class='form-group']/input[@name='name']")

    def inpt_name(self):
        return self.driver.find_element(*HomePage.name)

    shopbutton = (By.XPATH, "//a[text()='Shop']")

    def shop_button(self):
        self.driver.find_element(*HomePage.shopbutton).click()
        shoppage_obj = ShopPage(self.driver)
        return shoppage_obj
