import urllib3
import requests
from urllib import request


# request GET请求

def request36kr():
    # 忽略警告：InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.
    requests.packages.urllib3.disable_warnings()
    # 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
    http = urllib3.PoolManager()
    # 通过request()方法创建一个请求：
    # r = http.request('GET', 'http://www.baidu.com/')
    # print(r.status)  # 200
    # 获得html源码,utf-8解码
    # print(r.data.decode())

    # request GET请求(添加数据)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }

    r = http.request('GET',
                     'https://36kr.com/newsflashes',
                     # fields={'wd': 'hello'},
                     headers=header)

    print(r.status)  # 200
    print(r.data.decode())


if __name__ == "__main__":
    request36kr()
