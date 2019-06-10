from selenium import webdriver
import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

''' Connecting to Selenium Web Driver '''
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\\" + getpass.getuser() + r"\Automation")
driver = webdriver.Chrome(options=options)
driver.get('https://people.zoho.com/visualbisolutions/zp#reimbursement/form/listview-formId:249048000002801059/viewId:249048000002801061/typeOfView:self')
# driver.find_element_by_id("zp_views_field_Claim_From").click()
table =  driver.find_element_by_xpath("//table[@class='table table-hover Vlis  FLhead']")
i = 0

# mytable = driver.find_element_by_css_selector('table table-hover Vlis  FLhead')
# for row in mytable.find_elements_by_css_selector('tr'):
#     for cell in row.find_elements_by_tag_name('td'):
#         print(cell.text)

for row in table.find_elements_by_xpath(".//tr"):
    for td in row.find_elements_by_xpath(".//td[@id='zp_views_field_Claim_From']"):
        if td.text == '01-Jun-2019':
            driver.find_element_by_xpath(".//td[@id='zp_views_field_Claim_From']").click()
            try:
                element = WebDriverWait(driver, 200).until(
                    EC.presence_of_element_located((By.ID, "zp_appproval_comment_btn"))
                )
            finally:
                print("Found")
                driver.find_element_by_xpath('//a[@id="zp_appproval_comment_btn"]').click()
                # a = driver.find_element_by_id("zp_appproval_comment_btn").click()
                # print(a)



    # print([td.text for td in row.find_elements_by_xpath(".//td[@id='zp_views_field_Claim_From']")])
    # print(row.find_elements_by_xpath(".//td[@class='Approver']"))
    # print(driver.find_element_by_css_selector("value='#AprvImg'"))
    # (By.css("input[class~='required']"))
    #  print([td.title for td in row.find_elements_by_xpath(".//td[@class='AprvImg']")])
    

# driver.close()
