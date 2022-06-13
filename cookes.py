import time
import auth_data
from selenium import webdriver
import pickle


options = webdriver.ChromeOptions()


driver= webdriver.Chrome("C:/Users/dimitry/PycharmProjects/selenium/chromedriver.exe")


#url="https://vk.com/"
try:

    driver.maximize_window()
    #driver.get(url=url)
    #time.sleep(2)
    #driver.find_element_by_name("email").send_keys(auth_data.vk_email)
    #driver.find_element_by_name("pass").send_keys(auth_data.vk_password)
    #driver.find_element_by_css_selector("#mcont > div > div.fit_box.bl_cont.new_form > div > div > form > div.fi_row_new > input").click()


    #pickle.dump(driver.get_cookies(), open(f"{auth_data.vk_email}_cookies", "wb"))
    driver.get("https://vk.com/")
    for cookie in pickle.load(open(f"{auth_data.vk_email}_cookies", "rb")):
        driver.add_cookie(cookie)
        time.sleep(3)
        driver.refresh()
        time.sleep(5)
except Exception as ex:
    print(ex)