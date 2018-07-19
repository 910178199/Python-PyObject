import scrapy
import logging
import pymysql
# freebuf 新闻抓取

db = pymysql.connect("localhost", "root", "123456", "FREEBUF_DATA")
cursor = db.cursor()


class FreebufSpider(scrapy.Spider):
    name = 'freebuf'
    start_urls = [
        'http://www.freebuf.com/page/64',
    ]

    def parse(self, response):
        for news_list in response.css('div.news_inner'):
            url = news_list.css('div.news-img a::attr(href)').extract_first()
            title = news_list.css(
                'div.news-img img::attr(title)').extract_first()
            imgurl = news_list.css(
                'div.news-img img::attr(src)').extract_first()
            content = news_list.css('dd.text::text').extract_first()

            if title is not None:
                # 存入数据库
                dbInsert(url, title, imgurl, content)
                yield {
                    'url': url,
                    'title': title,
                    'imgurl': imgurl,
                    'content': content,
                }

            # 下一页数据
            # next_page = response.css(
            #     'div.news-more a::attr(href)').extract_first()
            # if next_page is not None:
            #     next_page = response.urljoin(next_page)
            #     yield scrapy.Request(next_page, callback=self.parse)


def dbInsert(url, title, imgurl, content):
    insertSql = """INSERT INTO NEWS(TITLE,URL,IMGURL,CONTENT) VALUES ('%s','%s','%s','%s')""" % (
        title, url, imgurl, str(content).strip().replace('\'', ' '))
    try:
        # 执行插入sql语句
        cursor.execute(insertSql)
        # 提交
        db.commit()
    except IOError as e:
        # 如果发生错误
        db.rollback()
        # 关闭数据库连接
        db.close()
        print("msg====="+e.message)