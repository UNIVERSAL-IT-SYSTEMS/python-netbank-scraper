import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dockerServerIP=os.popen("docker-machine ip default").read().strip()


driver = webdriver.Remote(command_executor='http://' + dockerServerIP + ':4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)

NETBANK_ID=os.environ.get('NETBANK_ID')
NETBANK_PASS=os.environ.get('NETBANK_PASS')


if NETBANK_ID == None or NETBANK_PASS == None:
	raise Exception('Please set NETBANK_ID and NETBANK_PASS')

#driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.my.commbank.com.au/netbank/Logon/Logon.aspx")

username = driver.find_element_by_name("txtMyClientNumber$field")
username.send_keys(NETBANK_ID)

password = driver.find_element_by_name("txtMyPassword$field")
password.send_keys(NETBANK_PASS)

login = driver.find_element_by_name("btnLogon$field")
login.click()

viewaccounts = driver.find_element_by_link_text("View accounts")
print "Click View Accounts"
viewaccounts.click()


accounts=driver.find_element_by_id("ctl00_ContentHeaderPlaceHolder_ddlAccount_field")
print "Clicking: ctl00_ContentHeaderPlaceHolder_ddlAccount_field"
accounts.click()
print "Hit Enter: ctl00_ContentHeaderPlaceHolder_ddlAccount_field"
accounts.send_keys(Keys.RETURN)

print "Find element: ddl_select_scroll"
ddlselectscroll=driver.find_element_by_class_name("ddl_select_scroll")

print "Find element: ddl_options"
ddloptions=driver.find_element_by_class_name("ddl_options")

print "Find element: li"
items = ddloptions.find_elements_by_tag_name("li")

for item in items:
    accounts=driver.find_element_by_id("ctl00_ContentHeaderPlaceHolder_ddlAccount_field")
    print "Clicking: ctl00_ContentHeaderPlaceHolder_ddlAccount_field"
    accounts.click()
    print "LI: " + item.text
    item.click()
    driver.implicitly_wait(10) 

    print "Hit Enter: ctl00_ContentHeaderPlaceHolder_ddlAccount_field"
    accounts.send_keys(Keys.RETURN)
    