from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from utils.data_reader import read_csv
import pytest

test_data=read_csv("tests/test_data.csv")
@pytest.mark.parametrize("data", test_data)
class CheckoutPage:
    checkout_btn=(By.ID, "checkout")
    first_name=(By.ID,"first-name")
    last_name=(By.ID,"last-name")
    postal_code=(By.ID,"postal-code")
    continue_btn=(By.ID,"continue")
    finish_btn=(By.ID,"finish")
    header_msg=(By.CLASS_NAME,"complete-header")
    price_check=(By.CLASS_NAME,"inventory_item_price")
    total_tag=(By.CLASS_NAME,"summary_subtotal_label")


    def __init__(self,driver):
        self.driver=driver

    def checkout(self):
      wait = WebDriverWait(self.driver, 10)
      checkout_btn = wait.until(
      EC.element_to_be_clickable(self.checkout_btn))
      checkout_btn.click()

    def address(self):
        self.driver.find_element(*self.first_name).send_keys("Gowtham")
        self.driver.find_element(*self.last_name).send_keys("M")
        self.driver.find_element(*self.postal_code).send_keys("638110")
        self.driver.find_element(*self.continue_btn).click()

    def finish(self):
       element=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.finish_btn))
       element.click()
       
    def get_success_message(self):
        msg = WebDriverWait(self.driver,10).until(
        EC.visibility_of_element_located(self.header_msg)
    )
        return msg.text

    def get_all_prices(self):
       elements=self.driver.find_elements(By.CLASS_NAME,"inventory_item_price") 
       prices=[]
       for el in elements:
          price_text= el.text
          price=float(price_text.replace("$",""))
          prices.append(price)
       return prices 
    
    def get_item_total(self):
     element = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
    
     text = element.text
     value = text.split("$")[1]

     return float(value)