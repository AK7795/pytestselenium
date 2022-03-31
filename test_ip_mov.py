'''import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    global  n1, n2, n3 , n4, n5, driver
    n1 = input("enter movie name :")
    n2 = input("enter release year :")
    n3 = input("enter director name :")
    n4 = input("enter distributor :")
    n5 = input("enter producer :")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(7)
    driver.close()


def test_3(setup):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("mname").send_keys(n1)
    driver.find_element_by_name("myear").send_keys(n2)
    driver.find_element_by_name("mdirector").send_keys(n3)
    driver.find_element_by_name("mdist").send_keys(n4)
    driver.find_element_by_name("mproducer").send_keys(n5)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[3]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[7]/td[2]/button").click()
    time.sleep(2)'''