import utilitis
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import fake_useragent
from fake_useragent import UserAgent
import webbrowser
user_agent =  ["helo world","zenit","top footbal"]
user= UserAgent()
options = webdriver.ChromeOptions()
#options.add_argument("--incognito")
#options.add_argument(f"user-agent={random.choice(user_agent)}")
#fake user agent
#options.add_argument(f"user-agent={user.safari}")
#fake user agent random
options.add_argument(f"user-agent={user.random}")
#options.add_argument("user-agent=hello world")

#two option for use webdriver
#driver = webdriver.Chrome
driver = webdriver.Chrome(executable_path="C:/Users/dimitry/PycharmProjects/selenium/chromedriver.exe",options=options)
url=("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")

try:

    driver.maximize_window()

    driver.get(url=url)
    #driver.fullscreen_window()

    time.sleep(2)
    #print(driver.title)
    #print(driver.current_url)
    #print(driver.current_window_handle)
    #driver.refresh()
    #time.sleep(3)
    driver.get_screenshot_as_file("C:/Users/dimitry/PycharmProjects/selenium/image/test1234.png")
    #driver.get_log("log.pdf")

    #driver.find_element_by_css_selector("#main_header > div > div.top_controls_h.td > div:nth-child(1)").click()
    #driver.get_screenshot_as_file("test3.png")
    #driver.get(url="https://selenium-python.readthedocs.io/waits.html")

    #time.sleep(5)

    #driver.get_screenshot_as_file("test2.png")
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()


