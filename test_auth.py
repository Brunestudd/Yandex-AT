import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
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


def is_element_displayed(driver, locator):
    try:
        return driver.find_element(*locator).is_displayed()
    except NoSuchElementException:
        return False


def test_valid_login(driver):
    driver.get("https://passport.yandex.ru/auth/")
    login_tumbler_locator = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button")
    login_field_locator = (By.XPATH, "//*[@id='passp-field-login']")

    if not is_element_displayed(driver, login_field_locator):
        driver.refresh()
        driver.find_element(*login_tumbler_locator).click()

    login_field = driver.find_element(*login_field_locator)
    login_field.send_keys('test123@gmail.com')


def test_invalid_login(driver):
    driver.get("https://passport.yandex.ru/auth/")
    login_tumbler_locator = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button")
    login_field_locator = (By.XPATH, "//*[@id='passp-field-login']")

    if not is_element_displayed(driver, login_field_locator):
        driver.refresh()
        driver.find_element(*login_tumbler_locator).click()

    login_field = driver.find_element(*login_field_locator)
    invalid_data = ["тест@mail.ru", "     ", "@@@@@@", ""]
    wait = WebDriverWait(driver, 10)

    for data in invalid_data:
        login_field.send_keys(Keys.CONTROL + "a")
        login_field.send_keys(Keys.DELETE)
        login_field.send_keys(data)
        submit_button = driver.find_element(By.XPATH, "//*[@id='passp:sign-in']")
        submit_button.click()
        error_message_locator = (By.XPATH, "//div[@id='field:input-login:hint']")

        error_message = wait.until(EC.visibility_of_element_located(error_message_locator))
        assert error_message.is_displayed()


def test_valid_phone(driver):
    driver.get("https://passport.yandex.ru/auth/")
    phone_tumbler_locator = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[2]/button")
    phone_field_locator = (By.XPATH, "//*[@id='passp-field-phone']")

    if not is_element_displayed(driver, phone_field_locator):
        driver.refresh()
        driver.find_element(*phone_tumbler_locator).click()

    phone_field = driver.find_element(*phone_field_locator)
    phone_field.send_keys('9276666666')


def test_invalid_phone(driver):
    driver.get("https://passport.yandex.ru/auth/")
    phone_tumbler_locator = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[2]/button")
    phone_field_locator = (By.XPATH, "//*[@id='passp-field-phone']")

    if not is_element_displayed(driver, phone_field_locator):
        driver.refresh()
        driver.find_element(*phone_tumbler_locator).click()

    phone_field = driver.find_element(*phone_field_locator)
    invalid_data = ["тест@mail.ru", "     ", "12345890", ""]
    wait = WebDriverWait(driver, 10)

    for data in invalid_data:
        phone_field.send_keys(Keys.CONTROL + "a")
        phone_field.send_keys(Keys.DELETE)
        phone_field.send_keys(data)
        submit_button = driver.find_element(By.XPATH, "//*[@id='passp:sign-in']")
        submit_button.click()
        error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-t='field:input-phone:hint']")))
        assert error_message.is_displayed()
