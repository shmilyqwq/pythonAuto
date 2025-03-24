# 浏览器驱动管理
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from src.core.config import config
from src.core.logger import logger

class Browser:
    def __init__(self):
        self.driver = None

    def start(self):
        browser_name = config["browser"]["name"]
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            if config["browser"]["headless"]:
                options.add_argument("--headless")
            self.driver = webdriver.Chrome(service=Service(), options=options)
        self.driver.implicitly_wait(config["browser"]["implicit_wait"])
        logger.info(f"Started {browser_name} browser")

    def quit(self):
        if self.driver:
            self.driver.quit()
            logger.info("Browser closed")