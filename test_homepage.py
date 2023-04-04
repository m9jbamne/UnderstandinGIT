import time

import pytest
import self
from selenium.webdriver.common.by import By
from Baseclass import Baseclass
from Pageobject.Homepage import HomePage
from Pageobject.ShopPage import ShopPage


class TestHomePage(Baseclass):
    # @pytest.mark.usefixtures("dataset")
    def test_homepage(self, dataset):
        # self.driver.implicitly_wait(2)
        homepage_obj = HomePage(self.driver)
        # homepage_obj.home_button()
        time.sleep(10)
        shoppage = homepage_obj.shop_button()
        products = shoppage.product_name()
        for product in products:
            if product.text == 'iphone X':
                print(product.text)
                product.click()
                break
        print(dataset)
        homepage_obj.inpt_name().send_keys(dataset[0])

    datadriven = Baseclass.dataload(self)

    @pytest.fixture(params=[datadriven])
    def dataset(self, request):
        return request.param
