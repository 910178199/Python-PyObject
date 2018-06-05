# selenium 的使用

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

execu_path = r'D:\huohu\geckodriver.exe'

# 模拟提交
def simulateSubmit():
    driver = webdriver.Firefox(executable_path=r'D:\huohu\geckodriver.exe')
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    print(driver.page_source)



if __name__ == "__main__":
    simulateSubmit()