import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import  auth_data
options = webdriver.ChromeOptions()

options.add_argument("user-agent")

driver= webdriver.Chrome("C:/Users/dimitry/PycharmProjects/selenium/chromedriver.exe",options=options)

url="https://vk.com/"
try:

    driver.maximize_window()
    driver.get(url=url)
    time.sleep(2)
    driver.find_element_by_name("email").send_keys(auth_data.vk_email)
    driver.find_element_by_name("pass").send_keys(auth_data.vk_password)
    #driver.find_element_by_css_selector("#mcont > div > div.fit_box.bl_cont.new_form > div > div > form > div.fi_row_new > input").click()
    driver.find_element_by_css_selector(
        "#mcont > div > div.fit_box.bl_cont.new_form > div > div > form > div.fi_row_new > input").send_keys(Keys.ENTER)


except Exception as ex:
    print(ex)

