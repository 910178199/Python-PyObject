import requests
# 请求图片
from PIL import Image
from io import BytesIO

# 获取需要的内容
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'
urlJson = 'https://api.github.com/events'


def requestGet():
    # r = requests.get(url)

    # 参数
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get(url, params=payload)
    # 设置编码
    print("url:" + r.url + '\n' + "encoding:" + r.encoding)
    r.encoding = 'UTF-8'
    print("requestGet:" + '\n' + r.text)


def requestPost():
    rPost = requests.post(url, data={'key': 'value'})
    rPost.encoding = 'UTF-8'
    print("requestPost" + "\n" + rPost.text)


def requestImg():
    rImg = requests.get('https://static.cnbetacdn.com/article/2018/0530/0fa58294de85391.png')
    # 不支持jpg图片
    img = Image.open(BytesIO(rImg.content))

    # 保存图片到本地
    # with open('img.png','wb') as file:
    #     file.write(rImg.content)
    print("\n" + "img" + str(img))


def requestJson():
    rJson = requests.get(urlJson)
    print("\n requestJson:" + str(rJson.json()))


# 定制请求头
def requestHeaders():
    url = 'https://36kr.com/newsflashes'
    # urlBook = 'http://www.biqukan.com/1_1094/5403177.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    data = requests.get(url, headers=headers)
    print('headers:')
    print(data.headers)
    print(data.text)

    # html.parser
    bf = BeautifulSoup(data.text, "html.parser")
    datas = bf.find_all("")
    print(datas)

if __name__ == '__main__':
    requestGet()
    requestPost()
    # requestImg()
    requestJson()
    requestHeaders()
