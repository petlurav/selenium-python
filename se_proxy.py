import time
from selenium import webdriver
from fake_useragent import UserAgent
import random
from seleniumwire import webdriver
options = webdriver.ChromeOptions()
#set proxy
options.add_argument("--proxy-server=138.128.91.65:8000")
proxy_option= {
    "proxy" :{"http":f""

}
}
driver= webdriver.Chrome("C:/Users/dimitry/PycharmProjects/selenium/chromedriver.exe",options=options)

#url=("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
url="https://2ip.ru/"

try:

    driver.maximize_window()

    driver.get(url=url)

    time.sleep(2)





except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
