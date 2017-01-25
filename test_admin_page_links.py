import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def test_admin_page_links(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").click()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").click()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//div[2]/button").click()
    sidebar_menu = driver.find_elements_by_css_selector("ul#box-apps-menu li#app-")
    for i in range(0,len(sidebar_menu)):
        sidebar_menu = driver.find_elements_by_css_selector("ul#box-apps-menu li#app-")
        sidebar_menu[i].click()
        driver.find_element_by_css_selector("h1")
        additional_menu = driver.find_elements_by_css_selector("ul.docs li")
        if len(additional_menu) != 0:
            for j in range(0, len(additional_menu)):
                additional_menu = driver.find_elements_by_css_selector("ul.docs li")
                additional_menu[j].click()
                driver.find_element_by_css_selector("h1")

