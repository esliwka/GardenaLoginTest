import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def browser():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_login_good_password(browser):
    browser.get("https://smart.gardena.com/")
    assert browser.title == "GARDENA smart system"

    browser.find_element(By.XPATH, "//form//input[@type='email']").send_keys("weyas57992@wowcg.com")
    browser.find_element(By.XPATH, "//form//input[@type='password']").send_keys("T3stP4ss")
    submit_button = browser.find_element(By.XPATH, "//form//button[@id='login-button']")
    WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(submit_button))
    submit_button.click()
    WebDriverWait(browser, 6).until(
        expected_conditions.url_matches("https://smart.gardena.com/#/gateway-setup/welcome"))
    assert browser.current_url == "https://smart.gardena.com/#/gateway-setup/welcome"


def test_login_bad_password(browser):
    browser.get("https://smart.gardena.com/")
    assert browser.title == "GARDENA smart system"

    browser.find_element(By.XPATH, "//form//input[@type='email']").send_keys("weyas57992@wowcg.com")
    browser.find_element(By.XPATH, "//form//input[@type='password']").send_keys("wrong")
    submit_button = browser.find_element(By.XPATH, "//form//button[@id='login-button']")
    WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(submit_button))
    submit_button.click()
    print("A")
    WebDriverWait(browser, 6).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "sguk-info-box-error")))
    print("A")
    assert browser.find_element(By.CLASS_NAME, "sguk-info-box-error").text == "The email address and the password don't match."
