from selenium import webdriver
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
        
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    option1 = browser.find_element_by_css_selector("[for=robotsRule]")
    option1.click()
    button.click()

finally:
    time.sleep(8)
    browser.quit()
