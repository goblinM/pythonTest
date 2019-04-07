'''
selenium 自动化测试工具，支持多种浏览器
爬虫中主要用来解决JavaScript渲染的问题
更多的可以查看api文档
https://selenium-python.readthedocs.io/api

启用 Headless（无头浏览器） 模式的方法
如下：
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome options=chrome _options)
'''
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# browser = webdriver.Chrome() #声明浏览器对象
# try:
#     browser.get(r'http://www.baidu.com') #访问页面
#     input = browser.find_element_by_id('kw')#查找元素id为kw
#     input.send_keys('Python')#设置值
#     input.send_keys(Keys.ENTER)#输入
#     wait = WebDriverWait(browser,10) #等待10s
#     wait.until(EC.presence_of_element_located((By.ID,'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookie())
#     print(browser.page_source)
# finally:
#     browser.close()

# 声明浏览器对象
# browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS()
# browser = webdriver.Safari()

#访问页面
# browser = webdriver.Chrome()
# browser.get('http://www.taobao.com')
# print(browser.page_source)
# browser.close()

#查找元素
# 单个元素 find_element...
# browser = webdriver.Chrome()
# browser.get('http://www.taobao.com')
# input_first = browser.find_element_by_id('q') # 元素ID为q
# input_second = browser.find_element_by_css_selector('#q') #css选择器
# input_third = browser.find_element_by_xpath('//*[@id="q"]') #xpath选择器
# print(input_first,input_second,input_third)
#通用查找的方法
# input_common = browser.find_element(By.ID,'q') #还有By.Class_Name等等
# print(input_common)
# browser.close()

# 多个元素 find_elements...
# browser = webdriver.Chrome()
# browser.get('http://www.taobao.com')
# input_common = browser.find_elements(By.ID,'q')
# print(input_common)

# find_element_by_name  通过元素名
# find_element_by_xpath 通过xpath查找
# find_element_by_link_text 通过link名查找
# find_element_by_partial_link_text
# find_element_by_tag_name #通过tag名查找
# find_element_by_class_name #通过类名查找
# find_element_by_css_selector #通过css选择器查找

#元素交互操作 send_keys() click_keys()
# browser = webdriver.Chrome()
# browser.get(r"http://www.taobao.com")
# input = browser.find_element_by_id('q')
# input.send_keys('IPhone') #输入值
# time.sleep(1)
# input.clear() #清空
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search') #获取button
# button.click() #点击

#交互动作
# browser = webdriver.Chrome()
# url = r"http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame("iframeResult") #获取嵌套的iframe
# source = browser.find_element_by_css_selector("#draggable") #css选择器
# target = browser.find_element_by_css_selector("#droppable")
# actions = ActionChains(browser)
# actions.drag_and_drop(source,target) #拖拽
# actions.perform()

#执行JavaScript
# browser = webdriver.Chrome()
# browser.get(r'https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

# 获取元素信息
# 获取属性 get_attribute()
# 获取文本 text
# 获取ID,位置，标签名，大小 id,location,tag_name,size
# browser = webdriver.Chrome()
# url = r"https://www.zhihu.com/explore"
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

# Frame
# browser = webdriver.Chrome()
# url = r"http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame("iframeResult") #获取嵌套的iframe 切换frame
# source = browser.find_element_by_css_selector("#draggable") #css选择器
# print(source)
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame() #回到原本的frame
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

#等待
#隐式等待 implicitly_wait()
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)

#显示等待
# browser = webdriver.Chrome()
# browser.get(r'https://www.taobao.com/')
# wait = WebDriverWait(browser,10)
# input = wait.until(EC.presence_of_element_located((By.ID,'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'btn-search')))
# print(input,button)

# title_is 标题是某内容
# title_contains 标题包含某内容
# presence_of_element_located 元素加载出，传入定位元素
# visibility_of_element_located 元素可见，传入定位元素
# visibility_of 可见，传入元素对象
# presence_of_all_elements_located 所有元素加载出
# text_to_be_present_in_element 某个元素文本包含某文字
# text_to_be_present_in_element_value 某个元素值包含某文字
# frame_to_be_avaliable_and_switch_to_it frame加载并切换
# invisibility_of_element_located 元素不可见
# element_to_be_clickable 元素可点击
# 更多看selenium-Python的官网api文档

#前进后退
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.get('https://www.taobao.com')
# browser.get('https://www.python.org')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()

#cookies  get_cookies()  add_cookie()
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({"name":"name","domain":"www.zhihu.com","value":"germy"})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

#选项卡管理
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')

#异常处理
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()