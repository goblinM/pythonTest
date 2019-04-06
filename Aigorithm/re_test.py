#!/usr/bin/python3
# _*_ coding:utf-8 _*_
"""
created by goblinM by 2019-03-06
正则表达式的一些例题
"""
import re

# 1.去除以下html文件中的标签，只显示文本信息。
# 把标签都去掉
s = "<div>\
<p>岗位职责：</p>\
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>\
<p><br></p>\
<p>必备要求：</p>\
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>\
<p>&nbsp;<br></p>\
<p>技术要求：</p>\
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>\
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>\
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>\
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>\
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>\
<p>&nbsp;<br></p>\
<p>加分项：</p>\
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>\
</div> \
"
s_sub = re.sub(r"</?\w+>|&nbsp;","",s)

#2.将以下网址提取出域名：
s2 = "http://www.interoem.com/messageinfo.asp?id=35`\
http://3995503.com/class/class09/news_show.asp?id=14\
http://lib.wzmc.edu.cn/news/onews.asp?id=769\
http://www.zy-ls.com/alfx.asp?newsid=377&id=6\
http://www.fincm.com/newslist.asp?id=415\
"
s2_sub = re.sub(r"(http://.+?/).+",lambda x:x.group(1),s2)
print(re.sub(r"(http://.+?/).+",lambda x:x.group(1),s2))

#3.提取单词
s3 = "hello world ha ha"
s3_split = re.split(r" ",s3)
print(s3_split)