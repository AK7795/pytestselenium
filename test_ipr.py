'''import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    global  n1, n2, n3 , n4, n5, n6, driver
    n1 = input("enter  name :")
    n2 = input("enter address :")
    n3 = input("enter pincode :")
    n4 = input("enter mobile :")
    n5 = input("enter email  :")
    n6 = input("enter password  :")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()


def test_3(setup):
    driver.get("https://iprimedtraining.herokuapp.com/userdata.php")
    time.sleep(1)
    driver.find_element_by_name("name").send_keys(n1)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[3]").click()
    time.sleep(1)
    driver.find_element_by_name("Address").send_keys(n2)
    time.sleep(1)
    driver.find_element_by_name("Pincode").send_keys(n3)
    time.sleep(1)
    driver.find_element_by_name("Mobile").send_keys(n4)
    time.sleep(1)
    driver.find_element_by_name("Email").send_keys(n5)
    time.sleep(1)
    driver.find_element_by_name("pass").send_keys(n6)
    time.sleep(1)
    driver.find_element_by_name("cnfpass").send_keys(n6)
    time.sleep(1)
    driver.find_element_by_name("fcheckbox").click()
    time.sleep(1)
    #driver.find_element_by_name("subbtn").click()
    #time.sleep(1)
    ac = ActionChains(driver)
    ac.context_click(driver.find_element_by_name("Pincode"))
    ac.perform()
    time.sleep(4)'''