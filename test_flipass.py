'''import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setUp():
    global  driver, name
    name = input("enter product : ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()


def test_flip1(setUp):

    driver.get("https://www.flipkart.com/")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    time.sleep(2)
    driver.find_element_by_name("q").send_keys(name)
    time.sleep(2)
    driver.find_element_by_class_name("L0Z3Pu").click()
    time.sleep(2)
    ac = ActionChains(driver)
    ele = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/div[2]/div[14]/div/div/div/a/div[2]/div[1]/div[1]")
    time.sleep(2)
    ac.move_to_element(ele)
    ac.click(ele)
    time.sleep(2)
    ac.perform()
    time.sleep(4)

'''