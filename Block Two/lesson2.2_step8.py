from selenium import webdriver
import time
import math
import os

link = "http://suninjuly.github.io/file_input.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Smit")
    input2 = browser.find_element_by_name("email")
    input2.send_keys("Smit@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '../file.txt')
    file_download = browser.find_element_by_id("file")
    file_download.send_keys(file_path)
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    time.sleep(8)
    browser.quit()