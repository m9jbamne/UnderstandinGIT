from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']/div/h4")

    def product_name(self):
        return self.driver.find_elements(*ShopPage.products)

