import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# option = webdriver.FirefoxOptions()
# option.add_argument('--no-sandbox')
# option.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Firefox(options=option)

def validate_required_filed(driver, url):

    driver.get(url)
    time.sleep(5)

    try:
        # accept cookie
        cookie_button = driver.find_element(By.ID, "cookie_action_close_header")
        cookie_button.click()
    except:
        pass

    # Submit test 
    submit_btn = driver.find_element(By.XPATH, "//button[@type='submit' and @class='pushbutton-wide' and text()='Submit']")
    # Scroll the button into view using JavaScript
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    time.sleep(3)
    submit_btn.click()
   
    
    # Required field error message
    required_field = driver.find_element(By.ID,"g1103-name-error")
    required_field.text == "Please fill out this field."   

    

def form_fillup(driver, url):
    
    driver.get(url)
    time.sleep(5)

    try:
        # accept cookie
        cookie_button = driver.find_element(By.ID, "cookie_action_close_header")
        cookie_button.click()
    except:
        pass

    # Enter Name
    name_filed = driver.find_element(By.ID, "g1103-name")
    name_filed.send_keys("Test Name")
    

    # Check Box1
    checkBox1_item = driver.find_element(By.ID,"g1103-whatisyourfavoritedrink-Water")
    checkBox1_item.click()

    # Check Box2
    checkBox2_item = driver.find_element(By.ID,"g1103-whatisyourfavoritecolor-Yellow")
    checkBox2_item.click()

    # Dropdown Test
    dropdown_element = driver.find_element(By.ID,"g1103-doyouhaveanysiblings")
    dropdown = Select(dropdown_element)
    dropdown.select_by_index(2)

    # Email Test
    email_field = driver.find_element(By.ID,"email")
    email_field.send_keys("test@gmail.com")

    message_filed = driver.find_element(By.ID, "contact-form-comment-message")
    message_filed.send_keys("Test Message")
    
    # Submit test 
    submit_btn = driver.find_element(By.XPATH, "//button[@type='submit' and @class='pushbutton-wide' and text()='Submit']")
    submit_btn.click()
    time.sleep(10)
    
    # Success message test
    successMessage = driver.find_element(By.ID,"contact-form-success-header")
    successMessage.text == "Your message has been sent"
    time.sleep(10)

    

if __name__ == '__main__':

    option = webdriver.FirefoxOptions()
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Firefox(options=option)

    url = "https://practice-automation.com/form-fields/"
    
    validate_required_filed(driver,url)
    form_fillup(driver,url)

    driver.quit()
    

    
 