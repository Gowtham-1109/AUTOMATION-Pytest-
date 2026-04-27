from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.logger import get_logger
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.log = get_logger(self.__class__.__name__)

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def load(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.log.info("Entering username")
        self.log.info("Entering password")
        self.log.info("Clicking login button")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()