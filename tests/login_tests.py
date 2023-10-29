from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome()
driver.maximize_window()


@pytest.fixture(autouse=True)
def setup():
    driver.get("https://the-internet.herokuapp.com/login")



def test_valid_login():
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        # assertions

        text = driver.find_element(By.ID, "flash").text
        assert text.__contains__("You logged into a secure area!")


 # def test_invalid_login_name():
    #     driver.find_element(By.ID, "username").send_keys("")  # set username
    #     driver.find_element(By.ID, "password").send_keys(
    #         "SuperSecretPassword!")  # set password
    #     driver.find_element(
    #         By.CSS_SELECTOR, "button.radius").click()  # click login

    #     # assertions

    #     text = driver.find_element(By.ID, "flash").text
    #     assert text.__contains__("Your username is invalid!")


    # def test_invalid_login_password():
    #     driver.find_element(By.ID, "username").send_keys(
    #         "tomsmith")  # set username
    #     driver.find_element(By.ID, "password").send_keys(" ")  # set password
    #     driver.find_element(
    #         By.CSS_SELECTOR, "button.radius").click()  # click login

    #     # assertions

    #     text = driver.find_element(By.ID, "flash").text
    #     assert text.__contains__("Your password is invalid!")
@pytest.mark.parametrize("user,pswd,message", [("tomsmith", "", "Your password is invalid!"), ("747347", "SuperSecretPassword!", "Your username is invalid!")])
def test_invalid_login(user, pswd, message):
        driver.find_element(By.ID, "username").send_keys(user)  # set username
        driver.find_element(By.ID, "password").send_keys(pswd)  # set password
        driver.find_element(
            By.CSS_SELECTOR, "button.radius").click()  # click login

        # assertions

        text = driver.find_element(By.ID, "flash").text
        assert text.__contains__(message)
