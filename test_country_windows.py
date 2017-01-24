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


def test_country_window(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    #get country links
    country_list = driver.find_elements_by_css_selector("table.dataTable a i.fa")
    #choosing random country to edit
    country_list[random.randrange(len(country_list))].click()
    #finding all links opening new windows
    external_links = driver.find_elements_by_css_selector("i.fa.fa-external-link")
    for external_link in external_links:
        country_window = driver.current_window_handle
        #opening new window
        external_link.click()
        time.sleep(5)
        all_windows = driver.window_handles
        all_windows.remove(country_window)
        new_window = all_windows[0]
        driver.switch_to_window(new_window)
        #closing new window
        driver.close()
        driver.switch_to_window(country_window)

