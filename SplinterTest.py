# Splinter Test 使用

import platform
import os
from time import sleep
from splinter import Browser

execu_path = r'D:\huohu\geckodriver.exe'


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

#验证码 我表示无能为力
def Channel_Oppo():
     with Browser(driver_name='chrome') as browser:
        url = "/html/body/nav/div/div/ul[1]/li[1]/a"
        browser.visit(url)
        select_plans = browser.find_by_xpath('//*[@id="beforeLogin"]/a[1]').click()
        browser.fill('name','18201523853')
        browser.fill('password','jaya.cc123')    


#Vivo有验证码  现阶段玩不了
def Channel_Vivo():
     with Browser(driver_name='chrome') as browser:
        url = "https://dev.vivo.com.cn/home"
        browser.visit(url)
        select_plans = browser.find_by_xpath('//*[@id="beforeLogin"]/a[1]').click()
        browser.fill('name','18201523853')
        browser.fill('password','jaya.cc123')



def CHannel_TengXun():
    with Browser(driver_name='chrome') as browser:
        url = "http://op.open.qq.com"
        browser.visit(url)
        select_plans = browser.find_by_xpath('//*[@id="switcher_plogin"]').first.click()
        browser.fill('u','3020170191')
        browser.fill('p','jaya.cc123')
        browser.find_by_xpath('//*[@id="login_button"]').click()
        browser.find_by_xpath('//*[@id="hnm-enterMemberCenter"]').click()
     
        project = ["1", "2", "3", "4"] 
        for i in project:
            appName = browser.find_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/div/div[3]/table/tbody/tr['+i+']/td[1]/span[2]').first
            print(appName.value)
            state = browser.find_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/div/div[3]/table/tbody/tr['+i+']/td[2]').first
            print(state.value)
            print('------------tengxun-----------')
        quit_browser(browser)



def CHannel_HuaWei():
    #,headless=True
    with Browser(driver_name='chrome') as browser:
        url = "https://developer.huawei.com/consumer/cn/"
        browser.visit(url)
        browser.find_by_xpath('//*[@id="befologin"]/a[1]').click()
        browser.fill('userAccount','18201523853')
        browser.fill('password','Jaya.cc123')
        browser.find_by_xpath('//*[@id="btnLogin"]').click()
        browser.find_by_xpath('//*[@id="hnm-enterMemberCenter"]').click()
        sleep(5)
        browser.find_by_xpath('/html/body/main/section/div/div[1]/div[1]/div[2]/div/div/div/div[2]').click()

      
        project = ["1", "2", "3", "4"] 
        for i in project:
            appName = browser.find_by_xpath('/html/body/main/section/div/div/div[1]/div[2]/div[1]/table/tbody/tr['+i+']/td[1]/a/span/p[1]').first
            print(appName.value)
            state = browser.find_by_xpath('/html/body/main/section/div/div/div[1]/div[2]/div[1]/table/tbody/tr['+i+']/td[4]/span').first
            print(state.value)
            print('------------huawei-----------')
        # quit_browser(browser)

def Channel_XiaoMi():
    with Browser(driver_name='chrome',headless=True) as browser:
        url = "https://dev.mi.com/console/"
        browser.visit(url)
        browser.find_by_xpath('/html/body/header/div/div[2]/div[1]/a[1]').click()
        browser.fill('user','18201523853')
        browser.fill('password','jaya.cc123')
        browser.find_by_xpath('//*[@id="login-button"]').click()

        browser.find_by_xpath('//*[@id="header_nav"]/ul/li[8]/a').click()
        browser.find_by_xpath('//*[@id="man"]/div/div[1]/ul/li[1]').click()

        project = ["1", "2", "3", "4"] 
        for i in project:
            #/html/body/div[1]/div[2]/div/div[2]/ul/li[3]/div/div[1]/div/p[1]
            appName = browser.find_by_xpath('/html/body/div[1]/div[2]/div/div[2]/ul/li['+i+']/div/div[1]/div/p[1]').first
            print(appName.value)
            state = browser.find_by_xpath('/html/body/div[1]/div[2]/div/div[2]/ul/li['+i+']/div/div[1]/div/p[5]').first
            print(state.value)
            print('------------xiaomi-----------')
        # quit_browser(browser)




def Channel_360():
    with Browser(driver_name="chrome") as browser:
        #360开发者平台
        # 访问 URL
        url = "http://dev.360.cn"
        browser.visit(url)
        # 找到并点击搜索按钮
        button = browser.find_by_xpath('//*[@id="statusBar"]/a[1]')
        # 与元素交互
        button.click()
        # 输入账号密码
        browser.fill('account', 'jingyinglutong@jaya.cc')
        browser.fill('password', 'jaya.cc123')
        loginBtn = browser.find_by_xpath('/html/body/div[13]/div[2]/div/div[2]/form/p[5]/input')
        loginBtn.click()
        browser.find_by_xpath('//*[@id="statusBar"]/a[3]').click()
        
        browser.find_by_xpath('/html/body').click()
        browser.find_by_xpath('/html/body').click()
        browser.find_by_xpath('/html/body').click()
        browser.find_by_xpath('/html/body').click()
        browser.find_by_xpath('/html/body').click()
        browser.find_by_xpath('/html/body').click()

        sleep(3)
        browser.find_by_xpath('//*[@id="side-menu"]/li[3]/a/span').click()

        project = ["1", "2", "3", "4"] 
        for i in project:
            appName = browser.find_by_xpath('//*[@id="home"]/a['+i+']').first
            print(appName.value)
            print('------------360-----------')

        # quit_browser(browser)


def Channel_Baidu():
    # incognito=True 匿名模式
    # , headless=True

    with Browser(driver_name="chrome", headless=True) as browser:
        #百度开发者平台
        url = "https://app.baidu.com/"
        browser.visit(url)
        browser.find_by_xpath('//*[@id="j-inheaderNew"]/div/ul[2]/li[2]/a/span').click()
        #输入账号密码
        browser.fill('userName','18201523853')
        sleep(10)
        browser.fill('password','jaya.cc123')
        #登陆
        browser.find_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()
        #延时5秒
        sleep(5)
        #移动鼠标
        browser.find_by_xpath('//*[@id="j-inheaderNew"]/div/ul[1]/li[1]/a/span').mouse_over()
        browser.find_by_xpath('//*[@id="j-inheaderNew"]/div/ul[1]/li[1]/a/span').click()
        browser.find_by_xpath('//*[@id="j-inheaderNew"]/div/ul[1]/li[1]/div/a[1]').click()
        project = ["1", "2", "3", "4"] 
        for i in project:
            appName = browser.find_by_xpath('//*[@id="divAppList"]/table/tbody/tr['+i+']').first
            print(appName.value)
            print('------------baidu-----------')
        # quit_browser(browser)


    

def quit_browser(browser=None):
    flag = input("Input q when you want to quit: ")
    if 'q' == str(flag):
        quit(browser)


if __name__ == "__main__":
    #渠道
    # Channel_Baidu()

    # Channel_XiaoMi()

    # CHannel_HuaWei()

    # Channel_360()

    #有问题
    # CHannel_TengXun()

