from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    wd.get("http://localhost/litecart/")
    assert "Online Store" in wd.title
    return wd

def test_shopping_cart(driver):
    for duck in range(1, 4):
        driver.find_element_by_css_selector("#box-most-popular img").click()
        if len(driver.find_elements_by_css_selector("span.required")) == 1:
            driver.find_element_by_name("add_cart_product").click()
            assert WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(duck)))
        else:
            Select(driver.find_element_by_name("options[Size]")).select_by_visible_text("Small")
            driver.find_element_by_name("add_cart_product").click()
        driver.back()

    driver.find_element_by_css_selector("div#cart a.link").click()

    cart_ducks = driver.find_elements_by_name("remove_cart_item")
    for i in range(len(cart_ducks)):
        driver.find_element_by_name("remove_cart_item").click()
        WebDriverWait(driver, 10).until(EC.staleness_of(driver.find_element_by_name("remove_cart_item")))
    cart_text = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "em")))
    assert cart_text.text == "There are no items in your cart."
