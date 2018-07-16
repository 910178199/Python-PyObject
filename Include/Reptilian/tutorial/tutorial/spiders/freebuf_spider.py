import scrapy
import logging

# freebuf 新闻抓取


class FreebufSpider(scrapy.Spider):
    name = 'freebuf'
    start_urls = [
        'http://www.freebuf.com/',
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
                yield {
                    'url': url,
                    'title': title,
                    'imgurl': imgurl,
                    'content': content,
                }

            # 下一页数据
            next_page = response.css(
                'div.news-more a::attr(href)').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
