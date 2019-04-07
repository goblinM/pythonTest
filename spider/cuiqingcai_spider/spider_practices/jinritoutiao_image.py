'''
分析ajax请求并抓取今日头条街拍美图
https://www.toutiao.com/ 头条网址
/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1554629117076
ajax需要传递的参数offset，format,keyword,autoload,count,cur_tab,aid,app_name,en_qc,from,pd
timestamp
'''
import os
import re
import time
from multiprocessing.pool import Pool
from urllib.parse import urlencode

import requests

from hashlib import md5


class toutiao:
    def __init__(self):
        #初始化
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

    def get_page(self,offset):
        #单个ajax请求
        params = {
            "aid":24,
            "app_name":"web_search",
            "offset":offset,
            "format":"json",
            "keyword":"街拍",
            "autoload":True,
            "count":20,
            "en_qc":1,
            "cur_tab":1,
            "from":"search_tab",
            "pd":"synthesis",
            "timestamp":""
        }

        url = r"https://www.toutiao.com/search_content/?"+urlencode(params)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
        except requests.ConnectionError:
            return None

    def get_image(self,data):
        #解析数据获取图片
        res = []
        if data.get("data"):
            for item in data.get("data"):
                if item.get('cell_type') is not None:#观察网站这个可知道，当这个出现时是没有图片链接的，需要排除
                    continue
                title = item.get("title")
                images = item.get("image_list")
                for image in images:
                    # res.append({"image":image.get("url"),"title":title})
                    yield {
                        "image":"https:"+image.get("url"),
                        "title":title
                    }


    def save_image(self,image):

        img_path = 'img' + os.path.sep +image.get("title").replace(".","") #这里有个问题当最后为...这样子会失去...导致没找到
        #保存图片
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        try:
            response = requests.get(image.get("image").replace("list", "large"))
            if response.status_code == 200:
                file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                    file_name=md5(response.content).hexdigest(),
                    file_suffix='jpg')
                if not os.path.exists((file_path)):
                    with open(file_path,'wb') as f:
                        f.write(response.content)
                    print('Downloaded image path is %s' % file_path)
                else:
                    print('Already Downloaded', file_path)
        except requests.ConnectionError:
            print('Failed to Save Image，item %s' % image)

def main(offset):
    obj = toutiao()
    data = obj.get_page(offset)
    for item in obj.get_image(data):
        print(item)
        obj.save_image(item)

if __name__ == "__main__":
    start = 1
    end = 2
    # obj = toutiao()
    # data = obj.get_page(20*1)
    # print(data['data'][0])
    pool = Pool() #多线程池,map()方法实现多线程下载
    group = [20*i for i in range(start,end+1)]
    pool.map(main,group)
    pool.close()
    pool.join()

