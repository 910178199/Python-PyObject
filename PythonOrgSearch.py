# selenium 搜索使用

# import unittest
from selenium import webdriver
# 调用键盘需要导入包
from selenium.webdriver.common.keys import Keys


execu_path = r'D:\huohu\geckodriver.exe'
phantomJs_path = r'D:\download\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe'

class PythonOrgSearch():

    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path=execu_path)

        # phantomJs不打开浏览器
        self.driver = webdriver.PhantomJS(executable_path=phantomJs_path)
    
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        # self.assertIn('Python',driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
        print(driver.page_source)


    def test_search_in_baidu(self):
        driver = self.driver
        # driver.implicitly_wait(3)
        driver.get("https://36kr.com/newsflashes")
        # elem = driver.find_element_by_name('wd')
        # elem.send_keys("python")
        # elem.send_keys(Keys.RETURN)
        print(driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    py = PythonOrgSearch()
    py.setUp()
    py.test_search_in_baidu()
    # py.test_search_in_python_org()
    # py.tearDown()
