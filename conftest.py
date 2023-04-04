import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"

    )


@pytest.fixture(scope="class")
def browser_invoke(request):
    browser_name = request.config.getoption("--browser_name")
    #chrome_option = webdriver.ChromeOptions("headless")
    if browser_name == "chrome":
        service_obj = Service("C:\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("C:\geckodriver-v0.31.0-win64\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    # driver.close()
    pass
