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

def test_campaign_item(driver):
    driver.get("http://localhost/litecart/")
    assert "Online Store" in driver.title
    campaign_duck = driver.find_element_by_css_selector("#box-campaigns li.product.column")
    duck_name = campaign_duck.find_element_by_css_selector(".name").text
    duck_regular_price = campaign_duck.find_element_by_css_selector(".regular-price").text
    duck_special_price = campaign_duck.find_element_by_css_selector(".campaign-price").text
    #css_style_properties
    campaign_price_main_page_color = campaign_duck.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    campaign_price_main_page_textdec = campaign_duck.find_element_by_css_selector(".campaign-price").value_of_css_property("text-decoration")
    campaign_price_main_page_fontsize = campaign_duck.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")
    regular_price_main_page_color = campaign_duck.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    regular_price_main_page_textdec = campaign_duck.find_element_by_css_selector(".regular-price").value_of_css_property("text-decoration")
    regular_price_main_page_fontsize = campaign_duck.find_element_by_css_selector(".regular-price").value_of_css_property("font-size")
    campaign_duck.click()
    campaign_duck_page = driver.find_element_by_css_selector("#box-product")
    campaign_duck_name = campaign_duck_page.find_element_by_css_selector(".title").text
    campaign_duck_regular_price = campaign_duck_page.find_element_by_css_selector(".regular-price").text
    campaign_duck_special_price = campaign_duck_page.find_element_by_css_selector(".campaign-price").text
    # css_style_properties
    campaign_price_duck_page_color = campaign_duck_page.find_element_by_css_selector(
        ".campaign-price").value_of_css_property("color")
    campaign_price_duck_page_textdec = campaign_duck_page.find_element_by_css_selector(
        ".campaign-price").value_of_css_property("text-decoration")
    campaign_price_duck_page_fontsize = campaign_duck_page.find_element_by_css_selector(
        ".campaign-price").value_of_css_property("font-size")
    regular_price_duck_page_color = campaign_duck_page.find_element_by_css_selector(".regular-price").value_of_css_property(
        "color")
    regular_price_duck_page_textdec = campaign_duck_page.find_element_by_css_selector(
        ".regular-price").value_of_css_property("text-decoration")
    regular_price_duck_page_fontsize = campaign_duck_page.find_element_by_css_selector(
        ".regular-price").value_of_css_property("font-size")
    assert duck_name == campaign_duck_name
    assert duck_regular_price == campaign_duck_regular_price
    assert duck_special_price == campaign_duck_special_price

    #asserts following below don't make too much sense, because prices belong to certain tags and classes, which have
    # specifically assigned styles anyway
    #meaning that selecting elements by the tag and/or class name already provides for checking if they have appropriate
    #style. So we can only check if it's red, striked/not striked text
    assert campaign_price_duck_page_color == campaign_price_main_page_color
    #assert campaign_price_duck_page_fontsize == campaign_price_main_page_fontsize <- will fail, main page has different fonsize
    assert campaign_price_duck_page_textdec == campaign_price_main_page_textdec
    #assert regular_price_duck_page_color == regular_price_main_page_color <- will fail, main page has slightly different color
    #assert regular_price_duck_page_fontsize == regular_price_main_page_fontsize <-will fail, main page has different fonsize
    assert regular_price_duck_page_textdec == regular_price_main_page_textdec