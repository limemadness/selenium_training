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

def test_sticker_is_present(driver):
    driver.get("http://localhost/litecart/")
    assert "Online Store" in driver.title
    ducks = driver.find_elements_by_css_selector("li.product.column")
    for duck in ducks:
        sticker = duck.find_elements_by_css_selector("div.sticker")
        assert len(sticker) == 1
        #if len(sticker) == 1:
        #    print("this duck is okay")
        #else:
        #   print("we got a faulty duck")


