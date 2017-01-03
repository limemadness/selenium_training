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
    duck_regular_price = campaign_duck.find_element_by_css_selector(".regular-price")
    duck_special_price = campaign_duck.find_element_by_css_selector(".campaign-price")
    duck_regular_price_txt = duck_regular_price.text
    duck_special_price_txt = duck_special_price.text

    #css_style_properties
    campaign_price_main_page_color = duck_special_price.value_of_css_property("color")
    campaign_price_main_page_textdec = duck_special_price.value_of_css_property("text-decoration")
    campaign_price_main_page_fontsize = duck_special_price.value_of_css_property("font-size")
    campaign_price_main_page_fontsize = campaign_price_main_page_fontsize[:-2]
    regular_price_main_page_color = duck_regular_price.value_of_css_property("color")
    regular_price_main_page_textdec = duck_regular_price.value_of_css_property("text-decoration")
    regular_price_main_page_fontsize = duck_regular_price.value_of_css_property("font-size")
    regular_price_main_page_fontsize = regular_price_main_page_fontsize[:-2]

    #opening duck page
    campaign_duck.click()
    campaign_duck_page = driver.find_element_by_css_selector("#box-product")
    campaign_duck_name = campaign_duck_page.find_element_by_css_selector(".title").text
    campaign_duck_regular_price = campaign_duck_page.find_element_by_css_selector(".regular-price")
    campaign_duck_special_price = campaign_duck_page.find_element_by_css_selector(".campaign-price")
    campaign_duck_regular_price_txt = campaign_duck_regular_price.text
    campaign_duck_special_price_txt = campaign_duck_special_price.text

    #css_style_properties
    campaign_price_duck_page_color = campaign_duck_special_price.value_of_css_property("color")
    campaign_price_duck_page_textdec = campaign_duck_special_price.value_of_css_property("text-decoration")
    campaign_price_duck_page_fontsize = campaign_duck_special_price.value_of_css_property("font-size")
    campaign_price_duck_page_fontsize = campaign_price_duck_page_fontsize[:-2]
    regular_price_duck_page_color = campaign_duck_regular_price.value_of_css_property("color")
    regular_price_duck_page_textdec = campaign_duck_regular_price.value_of_css_property("text-decoration")
    regular_price_duck_page_fontsize = campaign_duck_regular_price.value_of_css_property("font-size")
    regular_price_duck_page_fontsize = regular_price_duck_page_fontsize[:-2]

    #verifying item name and prices
    assert duck_name == campaign_duck_name
    assert duck_regular_price_txt == campaign_duck_regular_price_txt
    assert duck_special_price_txt == campaign_duck_special_price_txt

    #css style asserts
    assert regular_price_main_page_color != campaign_price_main_page_color
    assert regular_price_main_page_textdec != campaign_price_main_page_textdec
    assert int(float(regular_price_main_page_fontsize)) < int(float(campaign_price_main_page_fontsize))
    assert regular_price_duck_page_color != campaign_price_duck_page_color
    assert regular_price_duck_page_textdec != campaign_price_duck_page_textdec
    assert int(float(regular_price_duck_page_fontsize)) < int(float(campaign_price_duck_page_fontsize))

