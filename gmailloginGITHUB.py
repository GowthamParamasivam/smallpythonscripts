import selenium,time

from selenium import webdriver

#DOWNLOAD THE CHROME WEBDRIVER FROM THE INTERNET FOR AUTOMATING THE PROCESS IN THE CHROME WEB BROWSER
browser = webdriver.Chrome('LOCATION OF THE CHROME WEBDRIVER')
browser.maximize_window()

browser.get('https://www.google.com/gmail/')

#INSPECT THE ELEMENT IN LOGIN PAGE AND FIND THE FIELD TO ENTER THE DATA
email_field = browser.find_element_by_id('identifierId') 
email_field.clear()
email_field.send_keys('YOURMAILID@GMAIL.COM')

email_field_next = browser.find_element_by_id('identifierNext')
email_field_next.click()

time.sleep(2)

password_field = browser.find_element_by_name('password')
password_field.send_keys('YOUR MAIL ID PASSWORD')

password_next_button = browser.find_element_by_id('passwordNext')
password_next_button.click()

exit()

