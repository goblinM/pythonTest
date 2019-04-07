from lxml import etree

from lxml import _elementpath
text = '''
<div>
<ul>
    <li class='item-0'><a href='link1.html'>first item</a></li>
    <li class='item-1'><a href='link2.html'>second item</a></li>
    <li class='item-inactive'><a href='link3.html'>third item</a></li>
    <li class='item-0'><a href='link4.html'>fourth item</a></li>
    <li class='item-1'><a href='link5.html'>fifth item</a></li>
</ul>
</div>
'''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))#tostring()输出的是bytes类型，用decode()转换为str类型

#这是直接读取文本进行解析
# html = etree.parse('./test.html',etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))

#选取所有节点 *代表匹配所有的节点
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath("//*")
# print(result)

#子节点，通过/或//即可查找元素的子节点或子孙节点
# html = etree.parse("./test.html",etree.HTMLParser())
# result = html.xpath('//li/a') #查找所有li节点下的所有直接a子节点
# print(result)

#父节点 用..来实现,用parent::
# html = etree.parse("./test.html",etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/../@class') #用 ..实现
# result = html.xpath("//a[@href='link4.html']/parent::*/@class")
# #查找所有属性href=link4.html的a节点下的父节点属性有class的节点
# print(result)

#属性匹配 @
# html = etree.parse("./test.html",etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]')
# print(result)

#文本获取，text()方法
#获取 li 节点内部的文本，就有两种方式，一种是先选取a节点再获取文本，另一种就是使用//
# html = etree.parse(text,etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/a/text()')
# result2 = html.xpath('//li[@class="item-0"]//text()')
# print(result)

#属性获取 @
#属性匹配中括号加属性名和值来限定某个属性，如［＠href="linkl.html ”］，而此处的＠href 指的是获取节点的某个属性，二者需要做好区分
# html = etree.parse(text,etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# print(result)

#属性值多个匹配 contains(arg1,arg2) 第一个参数传入属性名称，第二个参数传入属性值
# text2 = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text2)
# result = html.xpath("//li[contains(@class,'li')]/a/text()")
# print(result)

#多属性匹配
#根据多个属性确定一个节点，使用运算符and来连接
# text2 = '''
# <li class="li li-first" name='item'><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text2)
# result = html.xpath("//li[contains(@class,'li') and @name='item']/a/text()")
# print(result)

#按序选择
# html = etree.HTML(text)
# result = html.xpath('//li[1]/a/text()') #第一个结点的文本值
# result2 = html.xpath('//li[last()]/a/text()') #最后一个结点的文本值
# result3 = html.xpath('//li[position()<3]/a/text()') #位置小于3的所有结点的文本值
# result4 = html.xpath('//li[last()-2]/a/text()') #倒数第三个的文本值

#节点轴选择
#XPath提供很多节点轴选择方法，包括获取子元素，兄弟元素，父元素，祖先元素等
html = etree.HTML(text)
result = html.xpath("//li[1]/ancestor::*") #ancestor获取所有的祖先节点
result2 = html.xpath("//li[1]/ancestor::div") #获取div祖先节点
result3 = html.xpath("//li[1]/attribute::*") #attribute获取所有的属性值
result4 = html.xpath("//li[1]/child::a[@href='link1.html']") #child获取所有直接子节点，获取所有href属性为link1.html的a节点
result5 = html.xpath("//li[1]/descendant::span") #descendant可以获取所有子孙节点，这里限定条件获取只包含span节点而不含a节点
result6 = html.xpath("//li[1]/following::*[2]") # following轴，获取当前节点之后的所有节点
result7 = html.xpath("//li[1]/following-sibling::*") #following-sibling，获取当前节点之后的所有同级节点。