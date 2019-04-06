import re
content1 ="Hello 123 4567 World_This is a Regex Demo"
# print(len(content1))
# result1 = re.match ("^Hello\s\d\d\d\s\d{4}\s\w{10}", content1)
content2 = "Hello 123456789 World_this is a regex Demo"
# result = re.match('^Hello\s(\d+)\sWorld',content2)
# result = re.match('^Hello.*Demo$',content1) # .任意字符  *无限多次
# .* 贪婪模式   .*? 非贪婪模式
# result = re.match('^He.*(\d+).*Demo$',content2)
result = re.match('^He.*?(\d+).*Demo$',content2)
#贪婪匹配下， ＊会匹配尽可能多的字符则表达式中．*后面是\d+，也就是至少一个数字，并没有指定具体多少个数字，
# 因此， 就尽可能匹配多的字符，这里就把 12345678 匹配了，给\d+留下一个可满足条件的数字 ，最后得到的内容就只有9
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())

content3 = '''Hello 1234567 World_This
is a Regex Demo
'''
# re.S 使.匹配包括换行在内的所有字符
# result = re.match('^He.*?(\d+).*Demo$',content3,re.S)
# print(result.group(1))
html = '''＜ div id="songs-list" >
<h2 class ＝"title"〉经典老歌</h2>
<p class="introduction"> 经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2"〉一路上有你</li>
<li data-view="7">
<a href ＝"/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href ="／3.mp3" singer="齐泰">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">尤辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5"><a href="/6.mp3" singer="邓丽君">但愿人长久</a></li>
</ul>
</div>'''
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# if result:
#     print(result.group(1), result.group(2))
# result = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
# print(result)
# print(type(result))
# for r in result:
#     print(result)
#     print(result[0],result[1],result[2])

# content4 = '54ak54yr5oiRcdhjas'
# content4 = re.sub('\d+',"",content4)
# print(content4)

# content5 = '2016-12-01 12:00'
# content6 = '2017-12-01 12:00'
# content7 = '2018-12-01 12:00'
# pattern = re.compile('\d{2}:\d{2}')
# result1 = re.sub(pattern,"",content5)
# result2 = re.sub(pattern,"",content6)
# result3 = re.sub(pattern,"",content7)
# print(result1+","+result2+","+result3)
html = """
<dd>
    <i class="board-index board-index-11">l1</i>
    <a href="/films/3667" title="辛德勒的名单" class="image-link" data-act="boarditem-click" data-val="{movieId:3667}">
      <img src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/b0d986a8bf89278afbb19f6abaef70f31206570.jpg@160w_220h_1e_1c" alt="辛德勒的名单" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
            <div class="movie-item-info">
                <p class="name"><a href="/films/3667" title="辛德勒的名单" data-act="boarditem-click" data-val="{movieId:3667}">辛德勒的名单</a></p>
                <p class="star">
                    主演：连姆·尼森,拉尔夫·费因斯,本·金斯利
                </p>
                <p class="releasetime">上映时间：1993-12-15(美国)</p>
            </div>
            <div class="movie-item-number score-num">
                <p class="score"><i class="integer">9.</i><i class="fraction">2</i></p>
            </div>
        </div>
    </div>
</dd>
"""
pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
items = re.findall(pattern,html)
print(items)
