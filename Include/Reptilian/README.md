### Scrapy目录结构：

scrapy.cfg: 项目的配置文件

tutorial/: 该项目的python模块。之后您将在此加入代码。

tutorial/items.py: 项目中的item文件.

tutorial/pipelines.py: 项目中的pipelines文件.

tutorial/settings.py: 项目的设置文件.

tutorial/spiders/: 放置spider代码的目录.

### 运行爬虫

scrapy crawl quotes
scrapy crawl freebuf

### 储存爬虫数据,第二次运行，在文件末尾追加数据

scrapy crawl quotes -o quotes.json
scrapy crawl freebuf -o freebuf.json

### 其他格式

scrapy crawl quotes -o quotes.jl

### 提取数据

scrapy shell 'http://freebuf.com'