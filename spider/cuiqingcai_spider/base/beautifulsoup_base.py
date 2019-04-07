html = """
<html><head><title>The Dormouse's story </title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story"> Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class= "sister" id="linkl"><!--Elsie--></a>,
<a href="http://example.com/lacie"  class= "sister" id="link2" >Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3”>Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">..</p> 
"""
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print(soup.prettify()) #代码格式补齐
# print(soup.title.string)

#标签选择器
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,'lxml')
# print(soup.title)
# print(type(soup.title))
# print(soup.head)
# print(soup.p)
#获取名称 name
# print(soup.title.name)
#获取属性 attrs[]
# print(soup.p.attrs['name'])
# print(soup.p['name'])
#获取内容 string
# print(soup.p.string)
#嵌套选择 .
# print(soup.head.title.string)
#子节点和子孙节点 contents
# print(soup.p.contents) #返回的是列表
#children 所有子节点
# print(soup.p.children)
# for i,child in enumerate(soup.p.children):
    # print(i,child)
#返回的是生成器类型
#获取所有的子孙节点，可以调用descendants属性
# print(soup.p.descendants)
# for i,child in enumerate(soup.p.descendants):
#     print(i,child)
#返回的是生成器类型
#某个节点的父节点 parent
#所有的祖先节点，parents
# print(soup.a.parent)
# print(soup.a.parents)
#兄弟节点 next_sibling和previous_sibling分别获取节点的下一个和上一个兄弟节点
#next_siblings和previous_siblings则分别返回前面和后面的兄弟节点的生成器
# print('next_sibling',soup.a.next_sibling)
# print('previous_sibling',soup.a.previous_sibling)
# print('next_siblings',list(enumerate(soup.a.next_siblings)))
# print('previous_siblings',list(enumerate(soup.a.previous_siblings)))

html2 = """
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
"""
# 方法选择器
# find_all(name,attrs,recursive,text,**kwargs)  返回所有的元素
from bs4 import BeautifulSoup
soup = BeautifulSoup(html2,'lxml')
# name参数查找
# print(soup.find_all(name='ul')) #等价于soup.find_all("ul")
# print(type(soup.find_all(name='ul')[0]))#查找ul
# for ul in soup.find_all(name='ul'):#查找ul下的li
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):#查找li的内容
#         print(li.string)
# attrs参数查找
# print(soup.find_all(attrs={"id":"list-1"}))
# print(soup.find_all(attrs={"name":"element"}))
# print(soup.find_all(id='list-1'))
# print(soup.find_all(class_='element'))
# text参数查找
# print(soup.find_all(text='Foo'))

# find(name,attrs,recursive,text,**kwargs)  返回单个的元素，方法使用和find_all()一致
# print(soup.find('ul'))
# print(soup.find('page'))

# find_parents()，find_parent()  返回祖先节点，返回父节点
# find_next_siblings(), find_next_sibling() 返回后面的兄弟节点，返回第一个兄弟节点
# find_previous_siblings(), find_previous_sibling()  返回前面所有兄弟节点，返回前面第一个兄弟节点
# find_all_next(), find_next() 返回节点后所有符合条件的节点，返回节点后第一个符合条件的节点
# find_all_previous() , find_previous() 返回节点前所有符合条件的节点，返回节点前第一个符合条件的节点

# CSS选择器
# select()直接传入CSS选择器即可完成选择
from bs4 import BeautifulSoup
soup = BeautifulSoup(html2,'lxml')
# print(soup.select('.panel .panel-body')) #选择类class .
# print(soup.select('#list-2 .element')) #选择id #
# print(soup.select('ul li')) #选择标签
# print(soup.select('ul')[0])

#迭代
for ul in soup.select('ul'):
    print(ul.select('li'))

#获取属性 []或者.attrs[]
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

#获取内容get_text()
for ll in soup.select('li'):
    print(ll.get_text())
