import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("executable_path=C:/chromedriver/chromedriver.exe")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def get_element(driver, locator):
    try:
        return driver.find_element(*locator)
    except NoSuchElementException:
        return None


def test_valid_login(driver):
    driver.get("https://passport.yandex.ru/auth/")
    login_locator = (By.XPATH,
                     "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div[2]/span/input")
    login_field = get_element(driver, login_locator)
    if not login_field:
        login_tumbler_locator = (By.XPATH,
                                 "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button")
        login_tumbler = driver.find_element(*login_tumbler_locator)
        login_tumbler.click()
        driver.refresh()
        login_field = driver.find_element(*login_locator)
    login_field.send_keys('test123@gmail.com')


def test_invalid_login(driver):
    driver.get("https://passport.yandex.ru/auth/")
    login_locator = (By.XPATH,
                     "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div[2]/span/input")
    login_field = get_element(driver, login_locator)
    if not login_field:
        login_tumbler_locator = (By.XPATH,
                                 "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button")
        login_tumbler = driver.find_element(*login_tumbler_locator)
        login_tumbler.click()
        driver.refresh()
        login_field = driver.find_element(*login_locator)

    invalid_data = ["тест@mail.ru", "     ", "1234567890", ""]
    wait = WebDriverWait(driver, 10)
    error_message_locator = (By.XPATH, "//div[@id='field:input-login:hint']")

    for data in invalid_data:
        login_field.clear()
        login_field.send_keys(data)
        submit_button_locator = (By.XPATH,
                                 "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/button")
        submit_button = driver.find_element(*submit_button_locator)
        submit_button.click()
        error_message = wait.until(EC.visibility_of_element_located(error_message_locator))
        assert error_message.is_displayed()


def test_valid_phone(driver):
    driver.get("https://passport.yandex.ru/auth/")
    phone_locator = (By.XPATH,
                     "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/span/input")
    phone_field = get_element(driver, phone_locator)
    if not phone_field:
        phone_tumbler_locator = (By.XPATH,
                                 "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[2]/button")
        phone_tumbler = driver.find_element(*phone_tumbler_locator)
        phone_tumbler.click()
        driver.refresh()
        phone_field = driver.find_element(*phone_locator)
    phone_field.send_keys('9276666666')


def test_invalid_phone(driver):
    driver.get("https://passport.yandex.ru/auth/")
    phone_locator = (By.XPATH,
                     "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/span/input")
    phone_field = get_element(driver, phone_locator)
    if not phone_field:
        phone_tumbler_locator = (By.XPATH,
                                 "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[2]/button")
        phone_tumbler = driver.find_element(*phone_tumbler_locator)
        phone_tumbler.click()
        driver.refresh()
        phone_field = driver.find_element(*phone_locator)

    invalid_data = ["тест@mail.ru", "     ", "1234567890", ""]
    wait = WebDriverWait(driver, 10)
    error_message_locator = (By.XPATH, "//div[@data-t='field:input-phone:hint']")

    for data in invalid_data:
        phone_field.clear()
        phone_field.send_keys(data)
        submit_button_locator = (By.XPATH,
                                 "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/button")
        submit_button = driver.find_element(*submit_button_locator)
        submit_button.click()
        error_message = wait.until(EC.visibility_of_element_located(error_message_locator))
        assert error_message.is_displayed()
