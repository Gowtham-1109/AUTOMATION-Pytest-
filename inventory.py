from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    filter_drop=(By.CLASS_NAME,"product_sort_container")
    productname=(By.CLASS_NAME,"inventory_item_name")
    add_to_cart_btns=(By.XPATH,"//button[contains(text(),'Add to cart')]")
    cart_badge=(By.CLASS_NAME,"shopping_cart_link")
    remove_btn=(By.XPATH, "//button[text()='Remove']")
    continue_shopping_btn=(By.XPATH, "//button[text()='Continue Shopping']")
   
    def __init__(self,driver):
        self.driver=driver

    def setfilter(self,value):
        wait=WebDriverWait(self.driver,10)
        dropdown=wait.until(EC.element_to_be_clickable(self.filter_drop))
        dropdown=self.driver.find_element(*self.filter_drop)
        select=Select(dropdown)
        select.select_by_value(value)
    def get_all_names(self):
        elements=self.driver.find_elements(*self.productname)
        return[el.text for el in elements]
    def add_first_and_last(self):
        buttons=self.driver.find_elements(*self.add_to_cart_btns)
        buttons[0].click()
        buttons[-1].click()
        
    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text
    def cart_item_remove(self):
        self.driver.find_element(*self.cart_badge).click()
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.presence_of_element_located(self.remove_btn))
        buttons=self.driver.find_elements(*self.remove_btn)
        buttons[0].click()
    def click_continue(self):
        self.driver.find_element(*self.continue_shopping_btn).click()
        

    def add_first(self):
        buttons=self.driver.find_elements(*self.add_to_cart_btns)
        buttons[0].click()
        
    def open_cart(self):
        element=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.cart_badge))
        element.click()
    def get_all_prices(self):
       elements=self.driver.find_element(By.CLASS_NAME,"inventory_item_price") 
       prices=[]
       for el in elements:
          price_text= el.text
          price=float(price_text.replace("$",""))
          prices.append(price)
       return prices 
        

        
    
    
        