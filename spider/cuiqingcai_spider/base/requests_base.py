import requests

#
r = requests.get(r"http://www.baidu.com/")
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# data = {
#     'name':"mary",
#     'age':19
# }
# r = requests.get(r'http://httpbin.org/get',params=data)
# # print(r.text)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))

# import re
# headers = {
#     'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X 10_11_4) AppleWebKit/537.36(KHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get(r'http://www.zhihu.com/explore',headers=headers)
# patterns = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles = re.findall(patterns,r.text)
# print(titles)

import requests
# r = requests.get('http://www.jianshu.com')
# # print(type(r.status_code), r.status_code)
# # print(type(r.headers), r.headers)
# # print(type(r.cookies), r.cookies)
# # print(type(r.url), r.url)
# # print(type(r.history), r.history)

# r = requests.get("https://www.baidu.com")
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+'='+value)


# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456789")
# r = s.get("http://httpbin.org/cookies")
# print(r.text)

# from requests_oauthlib import OAuthl
# url = 'https://api.twitter.com/1.1/account/verify credentials.json'
# auth = OAuth1 ('YOUR_APP_KEY','YOUR_APP_SECRET', 'USER_OAUTH_TOKEN','USER_OAUTH_TOKEN_SECRET')
# requests.get(url, auth=auth)

from requests import Request, Session
url ='http://httpbin.org/post'
data = {
'name': 'germey'
}
headers = {
    'User-Agent' :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)             Chrome/53 .0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)