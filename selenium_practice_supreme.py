'''selenium practice on Supreme'''
#Wes Smith
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome()
time.sleep(3)
#paste link of product
driver.get("https://www.supremenewyork.com/shop/jackets/j5ovygx7z/frm82zlny")
time.sleep(3)
#item finding
#driver.find_element_by_xpath('//*[@id="container"]/article[1]/div/a/img').click()
#atc button
driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
time.sleep(2)
#go to checkout
driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
time.sleep(2)

#enter checkout info
#name
driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys('John Smith')
time.sleep(2)
#email
driver.find_element_by_xpath('//*[@id="order_email"]').send_keys('john@john.com')
time.sleep(2)
#phone numb
driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys('1234567890')
#address
driver.find_element_by_xpath('//*[@id="bo"]').send_keys('1234 Home Drive')
#zip code (will autofill state/city)
driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys('74851')
time.sleep(2)
#CC Number
driver.find_element_by_xpath('//*[@id="nnaerb"]').send_keys('1234567812345678')
#cc month
driver.find_element_by_xpath('//*[@id="credit_card_month"]').send_keys('02')
#cc year
driver.find_element_by_xpath('//*[@id="credit_card_year"]').send_keys('2022')
#CVV
driver.find_element_by_xpath('//*[@id="orcer"]').send_keys('123')

#agree to terms & conditions button
driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
#click process payment
driver.find_element_by_xpath('//*[@id="pay"]/input').click()
