from socket import timeout  # time out feature
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
# this stoppes and error code returung 



driver = webdriver.Chrome() # teling driver to use chrome
driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=4184c172-0944-4309-8807-3f27580c4869&client-request-id=12439f45-e5bd-4322-81f4-58456e1fdb0e&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=4b4d1670-dac7-4d53-b6e2-4beda5448635&domain_hint=&sso_reload=true')
#url of webpage
time.sleep(2)
email = driver.find_element_by_xpath('//*[@id="i0116"]')# to find xpath highligth button input box , inspect element , then do it again , them the rigth click highlighted html and left click to copy Xpath
email.send_keys('H09.ljawando@students.haaf.org.uk')#sendkeys type keys
time.sleep(2)
button1= driver.find_element_by_xpath('//*[@id="idSIButton9"]')
button1.click()#clicks
time.sleep(2)
Password= driver.find_element_by_xpath('//*[@id="i0118"]')
Password.send_keys('Password1')
time.sleep(2)
button2 = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
button2.click()

time.sleep(2)
button3 = driver.find_element_by_xpath('//*[@id="KmsiCheckboxField"]')
button3.click()

time.sleep(2)
button4 = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
button4.click()

time.sleep(5)


button5  = driver.find_element_by_xpath('//*[@id="toast-container"]')
button5.click()

#ideas for next time 
#save all the pictures of the techers
# alllow me to enter class at specifit time 