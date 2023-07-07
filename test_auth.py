import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
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


def test_valid_login(driver):
    driver.get("https://passport.yandex.ru/auth/")
    login_tumbler = driver.find_element(By.XPATH,
                                        "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button")
    login_field = driver.find_element(By.XPATH,
                                      "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div[2]/span/input")
    try:
        assert login_field.is_displayed()
    except NoSuchElementException:
        login_tumbler.click()
    login_field = driver.find_element(By.XPATH,
                                      "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div[2]/span/input")
    login_field.send_keys('test123@gmail.com')


def test_invalid_login(driver):
    driver.get("https://passport.yandex.ru/auth/")
    login_tumbler = driver.find_element(By.XPATH,
                                        "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button")
    login_field = driver.find_element(By.XPATH,
                                      "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div[2]/span/input")
    try:
        assert login_field.is_displayed()
    except NoSuchElementException:
        login_tumbler.click()
        driver.refresh()
        login_field = driver.find_element(By.XPATH,
                                          "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div[2]/span/input")

    invalid_data = ["тест@mail.ru", "     ", "1234567890", ""]
    wait = WebDriverWait(driver, 10)

    for data in invalid_data:
        login_field.clear()
        login_field.send_keys(data)
        submit_button = driver.find_element(By.XPATH,
                                            "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/button")
        submit_button.click()
        error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='field:input-login:hint']")))
        assert error_message.is_displayed()


def test_valid_phone(driver):
    driver.get("https://passport.yandex.ru/auth/")
    phone_tumbler = (By.XPATH, "//button[contains(text(), 'Телефон')]")
# phone_tumbler = driver.find_element(By.XPATH,
    #                                     "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[2]/button")
    phone_field = driver.find_element(By.XPATH,
                                      "//*[@id='passp-field-phone']")
    try:
        assert phone_field.is_displayed()
    except NoSuchElementException:
        phone_tumbler.click()
        driver.refresh()
    phone_field = driver.find_element(By.XPATH,
                                      "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/span/input")
    phone_field.send_keys('9276666666')


def test_invalid_phone(driver):
    driver.get("https://passport.yandex.ru/auth/")
    phone_tumbler = driver.find_element(By.XPATH,
                                        "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[2]/button")
    phone_field = driver.find_element(By.XPATH,
                                      "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/span/input")
    try:
        assert phone_field.is_displayed()
    except NoSuchElementException:
        phone_tumbler.click()
        driver.refresh()
    phone_field = driver.find_element(By.XPATH,
                                          "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/span/input")

    invalid_data = ["тест@mail.ru", "     ", "1234567890", ""]
    wait = WebDriverWait(driver, 10)

    for data in invalid_data:
        phone_field.clear()
        phone_field.send_keys(data)
        submit_button = driver.find_element(By.XPATH,
                                            "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/button")
        submit_button.click()
        error_message = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@data-t='field:input-phone:hint']")))
        assert error_message.is_displayed()
