import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def test_new_item(driver):
    #open catalog
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element_by_xpath('//*[@id="content"]/div[1]/a[2]').click()
    #editing general information tab
    driver.find_element_by_link_text("General").click()
    driver.find_element_by_name("status").click()
    driver.find_element_by_name("name[en]").clear()
    driver.find_element_by_name("name[en]").send_keys("lime_green_duck")
    driver.find_element_by_name("code").clear()
    driver.find_element_by_name("code").send_keys("1234567890")
    driver.find_element_by_xpath("(//input[@name='categories[]'])[2]").click()
    driver.find_element_by_xpath("(//input[@name='product_groups[]'])[3]").click()
    driver.find_element_by_name("quantity").clear()
    driver.find_element_by_name("quantity").send_keys("4")
    driver.find_element_by_css_selector("[type=file").send_keys(os.path.abspath("rubber_duck_lime.jpeg"))
    driver.find_element_by_name("date_valid_from").click()
    driver.find_element_by_name("date_valid_from").send_keys("2017-01-20")
    driver.find_element_by_name("date_valid_to").click()
    driver.find_element_by_name("date_valid_to").send_keys("2018-01-20")
    #editing tab additional information
    driver.find_element_by_link_text("Information").click()
    Select(driver.find_element_by_name("manufacturer_id")).select_by_visible_text("ACME Corp.")
    driver.find_element_by_name("keywords").clear()
    driver.find_element_by_name("keywords").send_keys("rubber duck")
    driver.find_element_by_name("short_description[en]").clear()
    driver.find_element_by_name("short_description[en]").send_keys("lime rubber duck")
    driver.find_element_by_name("head_title[en]").clear()
    driver.find_element_by_name("head_title[en]").send_keys("Lime Duck")
    #editing price tab
    driver.find_element_by_link_text("Prices").click()
    driver.find_element_by_name("purchase_price").clear()
    driver.find_element_by_name("purchase_price").send_keys("22")
    Select(driver.find_element_by_name("purchase_price_currency_code")).select_by_visible_text("US Dollars")
    driver.find_element_by_name("prices[USD]").clear()
    driver.find_element_by_name("prices[USD]").send_keys("22.00")
    #saving new duck
    driver.find_element_by_name("save").click()

def test_new_item_added(driver):
    #open catalog
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element_by_css_selector("tr.row:nth-child(4) > td:nth-child(3)")
    assert driver.find_element_by_css_selector("tr.row:nth-child(4) > td:nth-child(3)").text == "lime_green_duck"


#    driver.find_element_by_css_selector("tr.row:nth-child(4) > td:nth-child(3)")
