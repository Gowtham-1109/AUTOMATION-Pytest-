from selenium import webdriver
from pages.login_page import *
from pages.inventory import *
from pages.checkout import *
from utils.logger import get_logger
import time
import pytest
from utils.data_reader import read_csv

test_data = read_csv("tests/test_data.csv")

@pytest.mark.parametrize("data", test_data)

def test_login_success(data):
    driver = webdriver.Chrome()
    driver.maximize_window()

    login_page = LoginPage(driver)

    login_page.load()
    login_page.login(data["username"],data["password"])

    assert "inventory" in driver.current_url, "Login failed"
    
    driver.quit()


@pytest.mark.parametrize("data", test_data)
def test_filter_az(driver,data):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.load()
    login_page.login(data["username"],data["password"])

    inventory_page.setfilter("az")
    assert "inventory" in driver.current_url

@pytest.mark.parametrize("data", test_data)
def test_add_first_and_last(driver,data):
    login_page=LoginPage(driver)
    inventory_page=InventoryPage(driver)
    login_page.load()
    login_page.login(data["username"],data["password"])
    inventory_page.setfilter("az")
    products=inventory_page.get_all_names()
    first=products[0]
    last=products[-1]
    inventory_page.add_first_and_last()
    assert inventory_page.get_cart_count()=="2","Failed to add items"
    inventory_page.cart_item_remove()
    inventory_page.click_continue()
    inventory_page.add_first()
    products=inventory_page.get_all_names()
    first=products[0]

@pytest.mark.parametrize("data", test_data)    
def test_checkout(driver,data):
    log = get_logger("test_checkout")
    log.info("Test started")
    login_page=LoginPage(driver)
    inventory_page=InventoryPage(driver)
    checkout_page=CheckoutPage(driver)
    log.info("Opening login page")
    login_page.load()
    log.info("Logging in")
    login_page.login(data["username"],data["password"])
    inventory_page.setfilter("az")
    products=inventory_page.get_all_names()
    first=products[0]
    last=products[-1]
    inventory_page.add_first_and_last()
    assert inventory_page.get_cart_count()=="2","Failed to add items"
    inventory_page.cart_item_remove()
    inventory_page.click_continue()
    inventory_page.add_first()
    products=inventory_page.get_all_names()
    first=products[0]
    inventory_page.open_cart()

    checkout_page.checkout()
    checkout_page.address()


    prices = checkout_page.get_all_prices()
    calculated_total = sum(prices)

    actual_total = checkout_page.get_item_total()

    assert calculated_total == actual_total

    checkout_page.finish()
    message = checkout_page.get_success_message()
    assert message == data["expected_message"]

    

    
    
    

