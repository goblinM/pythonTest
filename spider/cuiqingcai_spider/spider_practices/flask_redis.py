'''
用flask+redis维护代理
代理其实是需要买的，如西刺：http://www.xicidaili.com
果本机有相关代理软件的话，软件一般会在本机创建 HTTP SOCKS 代理服务，本机直接使
用此代理也可以
代理池要求：
    ·多站抓取，异步检测
    ·定时筛选，持续更新
    ·提供接口，易于提取
代理池架构：
    获取器 -->  过滤器 -->  代理队列  --> 定时检查
                                |
                                API
'''