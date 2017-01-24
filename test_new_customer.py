import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from random import choice
from string import ascii_lowercase
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    wd.get("http://localhost/litecart/")
    assert "Online Store" in wd.title
    request.addfinalizer(wd.quit)
    return wd

def test_new_customer(driver):
    register_link = driver.find_element_by_css_selector("#box-account-login tr:nth-child(5) a")
    register_link.click()
    #new user info
    driver.find_element_by_name("firstname").clear()
    driver.find_element_by_name("firstname").send_keys("Marina")
    driver.find_element_by_name("lastname").clear()
    driver.find_element_by_name("lastname").send_keys("Malinina")
    driver.find_element_by_name("address1").clear()
    driver.find_element_by_name("address1").send_keys("Moldavskaya 19-2")
    driver.find_element_by_css_selector(".select2-selection").click()
    driver.find_element_by_css_selector("input.select2-search__field").clear()
    driver.find_element_by_css_selector("input.select2-search__field").send_keys("United States" + Keys.ENTER)
    driver.find_element_by_name("postcode").clear()
    driver.find_element_by_name("postcode").send_keys("94103")
    driver.find_element_by_name("city").clear()
    driver.find_element_by_name("city").send_keys("Cheliabinsk")
    new_email = "lime" + ''.join(choice(ascii_lowercase) for i in range(10)) + "@mail.ru"
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(new_email)
    driver.find_element_by_name("phone").clear()
    driver.find_element_by_name("phone").send_keys("+7919999999")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("654321")
    driver.find_element_by_name("confirmed_password").clear()
    driver.find_element_by_name("confirmed_password").send_keys("654321")
    driver.find_element_by_name("create_account").click()
    # have to do it this way cause otherwise Zones are not active
    Select(driver.find_element_by_css_selector("tr:nth-child(5) td:nth-child(2) select")).select_by_visible_text("California")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("654321")
    driver.find_element_by_name("confirmed_password").clear()
    driver.find_element_by_name("confirmed_password").send_keys("654321")
    driver.find_element_by_name("create_account").click()
    #logout
    driver.find_element_by_link_text("Logout").click()

    #user credentials aka email, password
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(new_email)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("654321")
    driver.find_element_by_name("login").click()
    assert driver.find_element_by_css_selector("#box-account > h3:nth-child(1)").text == "Account"
    #logout
    driver.find_element_by_link_text("Logout").click()

