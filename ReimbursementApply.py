from selenium import webdriver
import getpass
import pywinauto
import shutil

# Connecting to Selenium Web Driver
options = webdriver.ChromeOptions()
# options.add_argument(r"user-data-dir=C:\Users\\" + getpass.getuser() + r"\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"user-data-dir=C:\Users\\" + getpass.getuser() + r"\Automation")
driver = webdriver.Chrome(options=options)
driver.get('https://people.zoho.com/visualbisolutions/zp#reimbursement/form/add-formLinkName:Reimbursement_Form')

# Fixed Values
invoice_amount = driver.find_element_by_name("Currency_11")
invoice_amount.clear()
invoice_amount.send_keys("1000")
from_date = driver.find_element_by_name("Claim_From")
from_date.clear()
from_date.send_keys("01-Jun-2019")
to_date = driver.find_element_by_name("Claim_To")
to_date.clear()
to_date.send_keys("30-Jun-2019")
invoice_date = driver.find_element_by_name("Date1")
invoice_date.clear()
invoice_date.send_keys("5-Jun-2019")
description = driver.find_element_by_name("Description")
description.send_keys("Dummy")
final_amount = driver.find_element_by_name("Currency_1")
final_amount.clear()
final_amount.send_keys("1000")

# Selectors
driver.find_element_by_xpath("//select[@name='Expense_Type']/option[text()='Phone & Internet']").click()
driver.find_element_by_xpath("//select[@name='Proof_Attached']/option[text()='Yes']").click()

# File Upload
click_upload = driver.find_element_by_name("Proof_Attachement_zip").click()

# Windows Interaction with Pop up
app = pywinauto.application.Application()
mainWindow = app['Open'] # main windows' title
ctrl=mainWindow['Edit'] 
ctrl.ClickInput()
ctrl.TypeKeys(r'"C:\Users\ramgopalanv\OneDrive - Visual Bi Solutions Inc\Laptop Back-up L080\Ram\Desktop\ACT Bills\2019\ACT Invoice - June.pdf"',with_spaces=True)
#ctrl.TypeKeys('dummy.txt') 
ctrlBis = mainWindow['Open'] # open file button
ctrlBis.ClickInput()

#Submitting the Reimbursement
#submit = driver.find_element_by_id("zp_forms_add_btn").click()