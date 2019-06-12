'''selenium practice'''
#Wes Smith
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://www.paycomonline.net/v4/ee/ee-login.php")
time.sleep(4)
#username input
usrname_xpath = '//*[@id="txtlogin"]'
usrname = driver.find_element_by_xpath(usrname_xpath)
#input username
usrname.send_keys('myusername')
time.sleep(3)
#pw input
pw_xpath = '//*[@id="txtpass"]'
pw = driver.find_element_by_xpath(pw_xpath)
pw.send_keys('mypass')
time.sleep(3)
#Last 4 of SSN Input
ssn_xpath ='//*[@id="userpinid"]'
ssn = driver.find_element_by_xpath(ssn_xpath)
ssn.send_keys('1234')
#click login buttown
login_button_xpath ='//*[@id="btnSubmit"]'
login_button = driver.find_element_by_xpath(login_button_xpath)
login_button.click()
#go to time management sheet
dropdown_menu_xpath = '//*[@id="icon-menu-slideout"]'
dropdown_menu = driver.find_element_by_xpath(dropdown_menu_xpath)
dropdown_menu.click()
