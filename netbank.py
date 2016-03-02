import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

NETBANK_ID=os.environ.get('NETBANK_ID')
NETBANK_PASS=os.environ.get('NETBANK_PASS')

driver = webdriver.Firefox()
driver.get("https://www.my.commbank.com.au/netbank/Logon/Logon.aspx")

username = driver.find_element_by_name("txtMyClientNumber$field")
username.send_keys(NETBANK_ID)

password = driver.find_element_by_name("txtMyPassword$field")
password.send_keys(NETBANK_PASS)

login = driver.find_element_by_name("btnLogon$field")
login.click()

viewaccounts = driver.find_element_by_link_text("View accounts")
viewaccounts.click()

accounts=driver.find_element_by_id("ctl00_ContentHeaderPlaceHolder_ddlAccount_field")
accounts.click()
accounts.send_keys(Keys.RETURN)

ddlselectscroll=driver.find_element_by_class_name("ddl_select_scroll")
ddloptions=driver.find_element_by_class_name("ddl_options")

items = ddloptions.find_elements_by_tag_name("li")
for item in items:
    item.text
    print item.text
    item.click()
