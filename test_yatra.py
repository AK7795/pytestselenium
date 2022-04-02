'''import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setUp():
    global  driver

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(6)
    driver.close()


def test_flip1(setUp):
    driver.get("https://www.yatra.com/")
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="BE_flight_origin_date"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="20/04/2022"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/section/div[1]/div/div[1]/section/div/div/div/div[1]/div[3]/div[1]/div[2]/ul/li/a/i').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="BE_flight_flsearch_btn"]').click()
    time.sleep(2)

    time.sleep(4)'''