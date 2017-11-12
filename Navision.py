import requests, bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import webelement
import webbrowser


browser = webdriver.Chrome()
def RefreshElement():
    global customer,Prj,Domain,Task,Phase,Place
    customer    = browser.find_element_by_id('cbCust_TextBox')
    Prj         = browser.find_element_by_id('cbProject_TextBox')
    Domain      = browser.find_element_by_id('cbDomain_TextBox')
    Task        = browser.find_element_by_id('cbTask_TextBox')
    Phase       = browser.find_element_by_id('cbPhase_TextBox')
    Place       = browser.find_element_by_id('cbPlace_TextBox')
    #return (customer,Prj,Domain,Task,Phase)




url = "https://navisionie.sogeti.com/summary.aspx"
browser.get(url)

acard       = browser.find_element_by_id('ctl00_MenuForm1_Hl_CardActivity')
acard.click()
RefreshElement()
customer.send_keys('C00075 - Fineos Corporation Ltd');
Prj.click()
RefreshElement()
Place       = browser.find_element_by_id('cbPlace_TextBox')
Place.send_keys('Home - Home')
Prj.click()
RefreshElement()

days = browser.find_elements_by_class_name('Calender_Line')
for day in days :
    print ("Element %s %s " % day.tag_name,day.text)

    
#customer.send_keys(Keys.ENTER)



#browser.execute_script("LoginSubmit('Log In')")







