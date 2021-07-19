from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/cats.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_id("button")

finally:
    time.sleep(8)
    browser.quit()