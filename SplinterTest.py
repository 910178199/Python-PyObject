# Splinter Test 使用

import platform
import os
from time import sleep
from splinter import Browser


execu_path = r'D:\huohu\geckodriver.exe'
phantomJs_path = r'D:\download\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe'


def browserTest():
    # incognito=True 匿名模式

    with Browser(driver_name="firefox", executable_path=r'D:\huohu\geckodriver.exe') as browser:
        # 访问 URL
        url = "http://baidu.com"
        browser.visit(url)
        browser.fill(
            'wd', 'splinter - python acceptance testing for web applications')
        # 找到并点击搜索按钮
        button = browser.find_by_xpath('//input[@type="submit"]')
        # 与元素交互
        button.click()

        if browser.is_text_present('splinter.readthedocs'):
            print("Yes, the official website was found!")
        else:
            print("No, it wasn't found... We need to improve our SEO techniques")


def browserChrome():
    # incognito=True 匿名模式

    with Browser(driver_name="chrome", headless=True) as browser:
        # 访问 URL
        url = "http://baidu.com"
        browser.visit(url)
        browser.fill('wd', 'python')
        # 找到并点击搜索按钮
        button = browser.find_by_xpath('//input[@type="submit"]')
        # 与元素交互
        button.click()
        print(browser.html)


if __name__ == "__main__":
    # browserTest()
    browserChrome()
