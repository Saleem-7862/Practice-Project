import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver")
class TestBrowser:

    def test_testing(self, driver):
        driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
        driver.find_element(By.ID, "password").send_keys("Learning@830$3mK2")
        driver.find_element(By.ID, "signInBtn").click()
        driver.find_element(By.LINK_TEXT, "Shop").click()
        products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        # time.sleep(5)
        for pro in products:
            productname = pro.find_element(By.XPATH, "div/h4/a").text
            if productname == "Blackberry":
                pro.find_element(By.XPATH, "div/button").click()
                # driver.find_element(By.XPATH, "//button[text()='Add ']").click()
        driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        driver.find_element(By.ID, "country").send_keys("ind")
        # wait = WebDriverWait(driver, 10)
        # checkbox = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        # checkbox.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India"))).click()
        # link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='checkbox checkbox-primary']")))
        # link.click()
        driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        message = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']").text

        assert "Success! Thank you!" in message, "message not matched in {}".format(message)