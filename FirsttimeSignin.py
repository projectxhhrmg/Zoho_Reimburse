from selenium import webdriver
import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

''' One Time Sign-in to get Cache '''
# mailid=<Enter Your Mail Id>
# password=<Enter Your Password>
''' Connecting to Selenium Web Driver '''
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\\" + getpass.getuser() + r"\Automation")
driver = webdriver.Chrome(options=options)
driver.get('https://accounts.zoho.com/signin?servicename=zohopeople&signupurl=https://www.zoho.com/people/signup.html')
# input_mail = driver.find_element_by_id("lid")
# input_mail.send_keys(mailid)
# password_mail = driver.find_element_by_id("pwd")
# password_mail.send_keys(password)
driver.find_element_by_id("signin_submit").click()

''' Browser Waits for 200 seconds to enter your login details and then closes the browser '''
try:
    element = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.ID, "apply_leave"))
    )
finally:
    driver.close()
