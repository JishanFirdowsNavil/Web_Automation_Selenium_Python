import time
from selenium import webdriver


option = webdriver.FirefoxOptions()
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
driver = webdriver.Firefox(options=option)

def google():
    driver.get("https://chromedriver.chromium.org/")
    time.sleep(5)
    


if __name__ == '__main_':
    google()


