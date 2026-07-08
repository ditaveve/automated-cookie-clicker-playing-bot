from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
#driver.quit()

class RunGame:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://ozh.github.io/cookieclicker/")

        language_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="langSelect-EN"]'))
        )
        language_button.click()
        self.available_upgrades = []
        self.count_upgrades = 0


    def click_cookie(self):
        while True:
            try:
                cookie_button = self.driver.find_element(By.ID, value="bigCookie")
                cookie_button.click()
                break
            except StaleElementReferenceException:
                continue

    def check_upgrade_availability(self):
        self.available_upgrades = self.driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
        self.count_upgrades = len(self.available_upgrades)
        if self.available_upgrades == []:
            return False
        else:
            return True


    def buy_upgrade(self):
        last_available_upgrade = self.available_upgrades[self.count_upgrades - 1]
        last_available_upgrade.click()

    def get_score(self):
        while True:
            try:
                return self.driver.find_element(By.ID, value="cookiesPerSecond").text.split(':')[1]
            except StaleElementReferenceException:
                continue
    
    def stop(self):
        self.driver.quit()
        
