import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
#def driver(request):
#    wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
#    print(wd.capabilities)
#    request.addfinalizer(wd.quit)
#    return wd
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def test_countries_sort(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").click()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").click()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//div[2]/button").click()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    #get country data
    countries = driver.find_elements_by_css_selector("#content tr.row")
    countries_timezone_url = []
    country_name = []
    #verify alphabetical order of country names
    for country in countries:
        country_name.append(country.find_element_by_css_selector("td:nth-child(5)").text)
    assert sorted(country_name) == country_name
    #get countries with multiple timezones
    for country in countries:
        if int(country.find_element_by_css_selector("td:nth-child(6)").text) > 0:
            countries_timezone_url.append(country.find_element_by_css_selector("td:nth-child(5) a").get_attribute("href"))
    #verify alphabetical order of timezones
    for country_timezone_url in countries_timezone_url:
        driver.get(country_timezone_url)
        timezone_list = driver.find_elements_by_css_selector("#table-zones td:nth-child(2)")
        del timezone_list[-1:]
        timezones = []
        for timezone in timezone_list:
            timezones.append(timezone.text)
        print(timezones)
        assert sorted(timezones) == timezones

