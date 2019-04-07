'''
selenium模拟浏览器抓取淘宝商品美食信息.pyquery解析商品的图片，名称，价格，
购买人数，店铺名称和店铺所在地信息
并且把结果保存到MongoDB
https://www.taobao.com
https://s.taobao.com/search?q=ipad&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306
params: q,imgfile,commend,ssid,search_type,sourceId,spm,initiative_id,ie
'''
import time
from urllib.parse import quote

import pymongo
from selenium import webdriver
# 构造一个URL：https://s.taobao.com/search?q=iPad 类似的，把q对应的值换一下就可以了
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
class taobao:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser,10)
        self.KEYWORD = 'IPad'

    def index_page(self,page):
        '''
        :param page: 页码
        :return:
        '''
        print('正在爬取第',page,'页')
        try:
            url = r'https://s.taobao.com/search?q='+quote(self.KEYWORD)
            self.browser.get(url)
            if page > 1: #跳转操作
                input = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input'))
                )#输入搜索

                submit = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form>span.btn.J_Submit'))
                )
                input.clear()
                input.send_keys(page)
                submit.click()
            self.wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active > span'),str(page))
            )
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
            self.get_products(page)#提取商品信息
        except TimeoutException:
            self.index_page(page)

    def get_products(self,page):
        #获取商品数据
        html = self.browser.page_source
        doc = pq(html)
        items = doc("#mainsrp-itemlist .items .item").items()
        for item in items:
            product = {
                "_id":str(page)+"_"+item.attr('data-index'),
                "image":"https:"+item.find('.pic .img').attr('data-src'),
                "price":item.find('.price').text(),
                "deal":item.find('.deal-cnt').text(),
                "title":item.find(".title").text(),
                "shop":item.find('.shop').text(),
                "location":item.find(".location").text()
            }
            print(product)
            self.save_to_mongo(product)

    def save_to_mongo(self,data):
        MONGO_URL = '127.0.0.1:27017'
        MONGO_DB = 'taobao'
        MONGO_COLLECTIONS = "products"
        client = pymongo.MongoClient(MONGO_URL)
        db = client[MONGO_DB]
        try:
            if db[MONGO_COLLECTIONS].insert(data):
                print("存储到MongoDB成功")
        except Exception:
            print("存储到MongoDB失败")

if __name__ == "__main__":
    """
    遍历每一页
    """
    MAX_PAGE = 100
    obj = taobao()
    for i in range(61,MAX_PAGE+1):
        obj.index_page(i)
        time.sleep(1)

