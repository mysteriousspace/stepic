from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_class_name("btn")
    button1.click()

    new_windows = browser.window_handles[1]
    browser.switch_to.window(new_windows)

    input1 = browser.find_element_by_id("input_value")
    x = input1.text
    y = calc(x)

    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    time.sleep(8)
    browser.quit()