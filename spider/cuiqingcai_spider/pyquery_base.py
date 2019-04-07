from pyquery import PyQuery as pq

html = """
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
<div class="wrap">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
"""
# 字符串初始化
doc = pq(html)
# print(doc('li'))

#URL初始化
# doc = pq(url=r'http://www.baidu.com')
# print(doc('head'))

#文件初始化
# doc = pq(filename='demo.html')
# print(doc('li'))

#基本CSS选择器
# print(doc("#container .list li"))

#查找元素
# 子节点 find()
# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')
# print(lis)
# print(type(lis))
# children()
# lis = items.children()
# print(lis)

# 父元素 parent()某个节点的父节点  parents()所有的祖先节点
# items = doc(".list")
# container = items.parent()
# container2 = items.parents()
# container3 = items.parents('.wrap')
# print(container)
# print(container2)

# 兄弟元素siblings()
# li = doc('.list .item-0active')
# print(li.siblings())
# print(li.siblings('.active'))

#遍历 items()多个元素
# lis = doc("li").items()
# for l in lis:
#     print(l)

#获取信息 空格要下一层
# a = doc(".item-0.active a")
# print(a)
# print(a.attr('href')) #获取属性
# print(a.attr.href)

#获取文本 text()
# a = doc(".item-0.active a")
# print(a.text())

#获取html  html()
# a = doc(".item-0.active")
# print(a)
# print(a.html())

#DOM操作
# addClass,removeClass
# ll = doc(".item-0.active")
# print(ll)
# ll.remove_class('active')
# print(ll)
# ll.add_class("active")
# print(ll)

#attr css
# ll = doc(".item-0.active")
# print(ll)
# ll.attr('name','link') #添加属性name=link
# print(ll)
# ll.css('font-size','19px')
# print(ll)

#remove
html2 = """
<div class="wrap">
    Hello,World
    <p>This is a map</p>
</div>
"""
# doc2 = pq(html2)
# wrap = doc2(".wrap")
# print(wrap.text())
# wrap.find('p').remove()
# print(wrap.text())

#伪类选择器
ll = doc("li:first-child") #第一个li结点
print(ll)
ll = doc("li:last-child") #最后一个li节点
print(ll)
ll = doc("li:nth-child(2)") #第二个li节点
print(ll)
ll = doc("li:gt(2)") #第三个li之后的li节点
print(ll)
ll = doc("li:nth-child(2n)") #偶数位置的li节点
print(ll)
ll = doc("li:contains(second)") #包含second文本的li节点
print(ll)