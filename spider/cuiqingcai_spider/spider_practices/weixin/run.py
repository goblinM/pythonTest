"""
利用上一节课获取的代理爬取微信公众号的文章，提取正文，发表日期，公众号等内容
爬取来源是搜狗微信，其连接是https://weixin.sougou.com
如果状态码是302,那么代表这个ip被封了
"""
from spider.cuiqingcai_spider.spider_practices.weixin.spider_file import Spider

if __name__ == '__main__':
    spider = Spider()
    spider.run()