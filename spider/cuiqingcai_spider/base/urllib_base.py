import urllib.request
#urllib.request.urlopen(url,data=None,[timeout,]*,cafile=None,capath=None,cadefault=False.context=None)
response = urllib.request.urlopen(r'https://www.python.org')
# print(response.read().decode('utf-8')) #这个返回抓取的内容
# print(type(response)) #返回的类型
# print(response.status) #返回的状态
# print(response.getheaders()) #返回的头部
# print(response.getheader('Server')) #返回头部的server,结果为nginx，表示是nginx搭建的

# data = bytes(urllib.parse.urlencode({"word":"hello"}),encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())

# import socket
# import urllib.error
# try:
#     response = urllib.request.urlopen(r'http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('Time Out')

# import urllib.request
# request = urllib.request.Request(r"http://python.org")
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# from urllib import request, parse
# url = r'http://httpbin.org/post'
# headers = {
#     'User-Agent ': 'Mozilla/4.0 (compatible; MSIE S. S; Windows NT)',
#     'Host':'httpbin.org'
# }
# dict = {
#     'name':'Nana'
# }
# data= bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method='post')
# response = request.urlopen(req)
# print(response. read().decode(' utf-8'))
#验证
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError
# username = 'username'
# password ='password'
# url = r'http: //localhost:sooo/'
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username , password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
# try:
#     result = opener.open(url)
#     html = result. read(). decode ('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)

#代理
# from urllib.error import URLError
# from urllib.request import ProxyHandler,build_opener
#
# proxy_handler = ProxyHandler({
# "http ":'http://127.0.0.1:9743 ',
# 'https':'https://127.0.0.1:9743 '
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open ('https://www.baidu.com')
#     print(response.read() .decode (' utf-8'))
# except URLError as e:
#     print(e .reason)

#cookies
# import http.cookiejar, urllib.request
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler )
# response = opener.open ('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)

#urlparse
from urllib.parse import urlparse
result= urlparse("http://www.baidu com/index .htr ser?id=S#comment")
print(type(result), result)