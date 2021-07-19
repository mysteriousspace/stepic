from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"
    
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    
    summ = int(x) + int(y)
    
    select = Select(browser.find_element_by_css_selector("select"))
    select.select_by_visible_text(str(summ))
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    time.sleep(8)
    browser.quit()
    
