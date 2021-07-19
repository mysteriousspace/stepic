from selenium import webdriver
import time

link = "https://SunInJuly.github.io/execute_script.html"
    
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    time.sleep(8)
    browser.quit()
    
