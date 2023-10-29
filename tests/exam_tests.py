from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep



driver = webdriver.Chrome()
driver.maximize_window()
def test_radio_buttons():
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    driver.find_element(By.XPATH,"(//input[@name='gender'])[1]").click() #male
    driver.find_element(By.XPATH,"(//input[@name='ageGroup'])[3]").click() # 15 - 50 
    driver.find_element(By.XPATH,"//button[text()='Get values']").click() # get values
    
    ## Assertions 
    
    gender = driver.find_element(By.CSS_SELECTOR,"span.genderbutton").text
    assert gender == 'Male'
    sleep(4)
    age = driver.find_element(By.CSS_SELECTOR,"span.groupradiobutton").text
    age == '15 - 50'
    sleep(3)
    
    
def test_google_logo():
    driver.get("https://www.google.com/")
    assert driver.find_element(By.CSS_SELECTOR,"img.lnXdpd").is_displayed()
    