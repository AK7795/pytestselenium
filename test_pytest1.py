'''import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setUp():
    global pr, driver
    pr = input("enter product to search : ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(6)
    driver.close()


def test_flip1(setUp):
    driver.get("https://www.flipkart.com/")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    time.sleep(2)
    driver.find_element_by_name("q").send_keys(pr)
    time.sleep(1)
    driver.find_element_by_class_name("L0Z3Pu").click()
    time.sleep(1)
    ac = ActionChains(driver)
    ac.context_click(driver.find_element_by_name("q"))
    ac.perform()
    time.sleep(4)
'''