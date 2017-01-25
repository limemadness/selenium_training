import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    wd.get("http://localhost/litecart/admin/")
    wd.find_element_by_name("username").click()
    wd.find_element_by_name("username").send_keys("admin")
    wd.find_element_by_name("password").click()
    wd.find_element_by_name("password").send_keys("admin")
    wd.find_element_by_xpath("//div[2]/button").click()
    request.addfinalizer(wd.quit)
    return wd


def test_check_logs(driver):
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    links = driver.find_elements_by_css_selector("#content td:nth-child(3) a")
    link_count = len(links)
    for i in range(0, link_count):
        if 'edit_product' in str(links[i].get_attribute("href")):
            links[i].click()
            browser_log = driver.get_log("browser")
            print(browser_log)
            assert browser_log == []
            driver.back()
            links = driver.find_elements_by_css_selector("#content td:nth-child(3) a")
    