'''
抓取猫眼电影的T100的电影名称，时间，评分，图片等信息
https://maoyan.com/board/4
'''
import json
import re
import time

import requests
from requests import RequestException


class MaoYan:
    def __init__(self):
        #初始化headers,路径
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }
    def get_html(self,url):
        #检查返回的状态码,正常访问返回首页源代码
        try:
            response = requests.get(url,headers=self.headers)
            if response.status_code == 200: #访问成功
                return response.text
            return None
        except RequestException:
            return None

    def get_one_data(self,html):
        #正则提取需要的数据,获取一页的数据
        pattern = re.compile(
            '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S
        )
        items = re.findall(pattern,html)
        res = []
        for item in items:
            res.append({
                'index':item[0],
                'image':item[1],
                'title':item[2],
                'actor':item[3].strip()[3:] if len(item[3]) > 3 else "",
                'time':item[4].strip()[5:] if len(item[4]) > 5 else "",
                'score':item[5].strip()+item[6].strip()
            })
        return res

    def wirte_to_file(self,content):
        #数据保存到数据库或者a不断追加写入文件
        with open('maoyandata.txt','a',encoding='utf-8') as f:
            f.write(json.dumps(content,ensure_ascii=False)+'\n')

if __name__ == '__main__':
    # url = r'https://maoyan.com/board/4'
    obj = MaoYan()
    for i in range(1,11):
        url = r'https://maoyan.com/board/4?offset='+str(10*i-10)
        html = obj.get_html(url)
        content = obj.get_one_data(html)
        obj.wirte_to_file(content)
        time.sleep(1)





