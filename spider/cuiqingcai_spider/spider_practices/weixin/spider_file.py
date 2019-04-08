import time
from urllib.parse import urlencode

import requests
from requests import Session, ReadTimeout
from pyquery import PyQuery as pq
from spider.cuiqingcai_spider.spider_practices.weixin.request import WeiXinRequest
from .config import *
from spider.cuiqingcai_spider.spider_practices.weixin.db import RedisQueue
from spider.cuiqingcai_spider.spider_practices.weixin.mysql import MySQL

# proxy = None #全局代理
class Spider:
    base_url = 'https://weixin.sogou.com/weixin'
    keyword = "受贿"
    headers = {
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        "Accept":"application/json, text/javascript, */*; q=0.01",
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'IPLOC=CN1100; SUID=6FEDCF3C541C940A000000005968CF55; SUV=1500041046435211; ABTEST=0|1500041048|v1; SNUID=CEA85AE02A2F7E6EAFF9C1FE2ABEBE6F; weixinIndexVisited=1; JSESSIONID=aaar_m7LEIW-jg_gikPZv; ld=Wkllllllll2BzGMVlllllVOo8cUlllll5G@HbZllll9lllllRklll5@@@@@@@@@@; LSTMV=212%2C350; LCLKINT=4650; ppinf=5|1500042908|1501252508|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1NDolRTUlQjQlOTQlRTUlQkElODYlRTYlODklOEQlRTQlQjglQTglRTklOUQlOTklRTglQTclODV8Y3J0OjEwOjE1MDAwNDI5MDh8cmVmbmljazo1NDolRTUlQjQlOTQlRTUlQkElODYlRTYlODklOEQlRTQlQjglQTglRTklOUQlOTklRTglQTclODV8dXNlcmlkOjQ0Om85dDJsdUJfZWVYOGRqSjRKN0xhNlBta0RJODRAd2VpeGluLnNvaHUuY29tfA; pprdig=ppyIobo4mP_ZElYXXmRTeo2q9iFgeoQ87PshihQfB2nvgsCz4FdOf-kirUuntLHKTQbgRuXdwQWT6qW-CY_ax5VDgDEdeZR7I2eIDprve43ou5ZvR0tDBlqrPNJvC0yGhQ2dZI3RqOQ3y1VialHsFnmTiHTv7TWxjliTSZJI_Bc; sgid=27-27790591-AVlo1pzPiad6EVQdGDbmwnvM; PHPSESSID=mkp3erf0uqe9ugjg8os7v1e957; SUIR=CEA85AE02A2F7E6EAFF9C1FE2ABEBE6F; sct=11; ppmdig=1500046378000000b7527c423df68abb627d67a0666fdcee; successCount=1|Fri, 14 Jul 2017 15:38:07 GMT',
        "Cookie":"CXID=99613EA5979E68A7EABFA53A79FEAA73; SUID=A5744DDA3565860A5B4CDB2D0005009B; SUV=0003174FDEF743B15B7A58C3B0784396; ad=TZllllllll2tKEnllllllVhtNPGlllllL6C1Iyllll9lllll4Vxlw@@@@@@@@@@@; IPLOC=CN4301; ld=HZllllllll2tXAc6lllllVh$iSllllllL6C1Iyllll9llllljllll5@@@@@@@@@@; LSTMV=183%2C283; LCLKINT=2667; ABTEST=0|1554705889|v1; weixinIndexVisited=1; sct=1; JSESSIONID=aaagUoKXxI5tZhDrJFCNw; PHPSESSID=1cqoeg1p84uensci35cf3p6ob4; SNUID=A97F46D60C0989F3A74CA3480CE99F0D",
        'Host': 'weixin.sogou.com',
        'Upgrade-Insecure-Requests': '1',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        'User-Agent': "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }
    # requests.adapters.DEFAULT_RETRIES = 5
    session = Session()
    session.keep_alive = False
    queue = RedisQueue()
    mysql = MySQL()

    def get_proxy(self):
        '''
        从代理池获取代理
        :return:
        '''
        try:
            response = requests.get(PROXY_POOL_URL)#PROXY_POOL_URL http://221.7.255.168:8080
            if response.status_code == 200:
                print("Get Proxy",response.text)
                return response.text
            return None
        except requests.ConnectionError:
            return None

    def start(self):
        """
        初始化工作
        """
        # 全局更新Headers
        self.session.headers.update(self.headers)
        start_url = self.base_url + '?' + urlencode({'query': self.keyword, 'type': 2})
        weixin_request = WeiXinRequest(url=start_url, callback=self.parse_index, need_proxy=True)

        # 调度第一个请求
        self.queue.add(weixin_request)

    def parse_index(self, response):
        """
        解析索引页
        :param response: 响应
        :return: 新的响应
        """
        doc = pq(response.text)
        items = doc('.news-box .news-list li .txt-box h3 a').items()
        for item in items:
            url = item.attr('data-share')
            weixin_request = WeiXinRequest(url=url, callback=self.parse_detail)
            yield weixin_request
        next = doc('#sogou_next').attr('data-share')
        if next:
            url = self.base_url + str(next)
            weixin_request = WeiXinRequest(url=url, callback=self.parse_index, need_proxy=True)
            yield weixin_request

    def parse_detail(self, response):
        """
        解析详情页
        :param response: 响应
        :return: 微信公众号文章
        """
        doc = pq(response.text)
        data = {
            'title': doc('.rich_media_title').text(),
            'content': doc('.rich_media_content').text(),
            'dates': doc('#post-date').text(),
            'nickname': doc('#js_profile_qrcode > div > strong').text(),
            'wechat': doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        }
        yield data

    def request(self, weixin_request):
        """
        执行请求
        :param weixin_request: 请求
        :return: 响应
        """
        try:
            print(weixin_request.need_proxy)
            if weixin_request.need_proxy:
                proxy = self.get_proxy()
                if proxy:
                    print("KKKK",proxy)
                    # proxies = {
                    #     'http': 'http://' + proxy,
                    #     'https': 'https://' + proxy
                    # }
                    proxies = {
                        "http": "http://221.7.255.168:8080",
                        "https": "http://221.7.255.168:8080",
                    }
                    print(proxies)
                    return self.session.send(weixin_request.prepare(),
                                             timeout=weixin_request.timeout, allow_redirects=False, proxies=proxies)
            return self.session.send(weixin_request.prepare(), timeout=weixin_request.timeout, allow_redirects=False)
        except (ConnectionError, ReadTimeout) as e:
            print(e.args)
            # print("Proxy连接错误")
            return False

    def error(self, weixin_request):
        """
        错误处理
        :param weixin_request: 请求
        :return:
        """
        weixin_request.fail_time = weixin_request.fail_time + 1
        print('Request Failed', weixin_request.fail_time, 'Times', weixin_request.url)
        if weixin_request.fail_time < MAX_FAILED_TIME:
            self.queue.add(weixin_request)

    def schedule(self):
        """
        调度请求
        :return:
        """
        while not self.queue.empty():
            weixin_request = self.queue.pop()
            callback = weixin_request.callback
            print('Schedule', weixin_request.url)
            response = self.request(weixin_request)

            if response and response.status_code in VALID_STATUSES:
                results = list(callback(response))
                print(results)
                if results:
                    for result in results:
                        print('New Result', type(result))
                        if isinstance(result, WeiXinRequest):
                            self.queue.add(result)
                        if isinstance(result, dict):
                            self.mysql.insert('articles', result)
                else:
                    self.error(weixin_request)
            else:
                self.error(weixin_request)

    def run(self):
        """
        入口
        :return:
        """
        self.start()
        self.schedule()

if __name__ == '__main__':
    spider = Spider()
    spider.run()