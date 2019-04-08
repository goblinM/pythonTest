"""
测试搜狗微信
"""
import requests
from pyquery import PyQuery as pq
#page
url = r"https://weixin.sogou.com/weixin?type=2&query=受贿"
headers = {
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
        'User-Agent': "'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'"
    }

proxies = {
  "http": "http://221.7.255.168:8080",
  "https": "http://221.7.255.168:8080",
}

response = requests.get(url,headers=headers,proxies=proxies)
print(response.status_code)
doc = pq(response.text)
items = doc('.news-box .news-list li .txt-box h3 a').items()
for item in items:
    url = item.attr('data-share')
    print(url)
    res2 = requests.get(url)
    doc1 = pq(res2.text)
    data = {
        'title': doc1('.rich_media_title').text(),
        'content': doc1('.rich_media_content').text(),
        'dates': doc1('#post-date').text(),
        'nickname': doc1('#js_profile_qrcode > div > strong').text(),
        'wechat': doc1('#js_profile_qrcode > div > p:nth-child(3) > span').text()
    }
    print(data)