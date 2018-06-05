# -*- coding:UTF-8 -*-
import json

import requests
# 禁用安全请求警告
from urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if __name__ == '__main__':
    target = 'http://unsplash.com/napi/feeds/home'
    req = requests.get(url=target, verify=False)
    data = json.loads(req.text)
    next_page = data['next_page']
    print("下一页地址："+next_page)
    for item in data['photos']:
        print("图片ID：" + item['id'])
