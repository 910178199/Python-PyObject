from PIL import Image
import pytesseract

# 上面都是导包，只需要下面这一行就能实现图片文字识别
# ,lang='chi_sim'
# text=pytesseract.image_to_string(Image.open('20170608124203095.png'))
# print(text)


# -*-coding:utf-8-*-
import importlib
import sys
importlib.reload(sys)

import time
time1 = time.time()
from PIL import Image
import pytesseract

# 二值化算法
def binarizing(img, threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img


image = Image.open('20170608124203095.png')

# 去除干扰线算法
def depoint(img):  # input: gray image
    pixdata = img.load()
    w, h = img.size
    for y in range(1, h-1):
        for x in range(1, w-1):
            count = 0
            if pixdata[x, y-1] > 245:
                count = count + 1
            if pixdata[x, y+1] > 245:
                count = count + 1
            if pixdata[x-1, y] > 245:
                count = count + 1
            if pixdata[x+1, y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x, y] = 255
    return img



# 转化为灰度图
img = image.convert('L')
# 把图片变成二值图像。    
img1 = binarizing(img, 190)
# img2=depoint(img1)
img1.show()
code = pytesseract.image_to_string(img1)
print ("识别该验证码是:" + str(code))
