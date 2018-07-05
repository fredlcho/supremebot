from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import time



####### -- INSERT SUPREME LINKS HERE -- ######
#supremeitems= ['http://www.supremenewyork.com/shop/jackets/uwqb7hkfj'] #KEEP LINKS IN BETWEEN QUOTES(' ') AND SEPARATED BY COMMAS (,)
####### -- INSERT SUPREME LINKS HERE -- ######
#'http://www.supremenewyork.com/shop/all/accessories'
driver = webdriver.Chrome()
#driver = webdriver.Firefox(executable_path=r"C:\Program Files\Mozilla Firefox\geckodriver.exe")
driver.get('http://www.supremenewyork.com/shop/all/accessories')
#driver.find_element_by_link_text('Advanced Elements® Packlite™ Kayak').click()
time.sleep(1)
driver.find_element_by_link_text('Supreme®/Hanes® Checker Boxer Briefs (2 Pack)').click()
#for x in supremeitems:
#    driver.get(x)
time.sleep(1)
driver.implicitly_wait(1)
driver.find_element_by_name("commit").click()
#    driver.implicitly_wait(1)


time.sleep(1)
driver.find_element_by_link_text("checkout now").click()

driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[(@id = "order_billing_name")]').send_keys("Frederick Ho")
time.sleep(1)
driver.find_element_by_xpath('//*[(@id = "order_email")]').send_keys("fredericklcho@gmail.com")
driver.find_element_by_xpath('//*[(@id = "order_tel")]').send_keys("222-333-4444")
driver.find_element_by_xpath('//*[(@id = "bo")]').send_keys("673 Rab 82nd st")
time.sleep(1)
driver.find_element_by_xpath('//*[(@id = "oba3")]').send_keys("8S") 
driver.find_element_by_xpath('//*[(@id = "order_billing_zip")]').send_keys("83292")
driver.find_element_by_xpath('//*[(@id = "nnaerb")]').send_keys("8888 5555 6158 4751")
time.sleep(2)
Select(driver.find_element_by_xpath('//*[(@id = "credit_card_month")]')).select_by_visible_text('66')
Select(driver.find_element_by_xpath('//*[(@id = "credit_card_year")]')).select_by_visible_text('4444')
driver.find_element_by_xpath('//*[(@id = "orcer")]').send_keys("812")
driver.find_element_by_xpath('(//*[contains(concat( " ", @class, " " ), concat( " ", "iCheck-helper", " " ))])[2]').click()
#time.sleep(15)
driver.find_element_by_xpath('//*[(@id = "pay")]//input').click()
        ##--------------##
    ##                      ##
## ~ keep all formats the same ~ ##
    ##                      ##
        ##--------------##

## VV CHANGE NAME HERE VV ##
#Name.send_keys("Frederick Ho")
## VV CHANGE EMAIL HERE VV ##
#email.send_keys("fredericklcho@gmail.com")
## VV CHANGE PHONE NUMBER HERE VV ##
#tel.send_keys("111-111-1111")
## VV CHANGE ADDRESS HERE VV ##
#address.send_keys("1111 pink 32nd st")
## VV IF YOU LIVE IN APT/SUITE, CHANGE HERE, OTHERWISE PUT A "#" IN FRONT OF THE LINE, ex: #aptunit.send_keys("0S") VV ##
#aptunit.send_keys("5T")                 
## VV CHANGE ZIP CODE HERE VV ##
#zipcode.send_keys("45321")
## VV CHANGE CARD NUMBER HERE VV ##
#creditcard.send_keys("1111 1111 1111 1111")
## VV CHANGE CARD MONTH EXPIRATION HERE VV ##
#dropmonth.select_by_visible_text('11')
## VV CHANGE CARD YEAR EXPIRATION HERE VV ##
#dropyear.select_by_visible_text('2222')
# VV CHANGE CARD 3-DIGIT CVV HERE VV ##
#cvv.send_keys("556")


#checkbox.click()


