"""
goblinM created 2019-03-04
文件打开
"""
with open(r"C:\Users\君莫笑\Desktop\work and study\数据库表修改.txt",'r',encoding='utf-8') as f:
    for l in f.readlines():
        print(l)

#打开文件写入：
with open(r"C:\Users\君莫笑\Desktop\work and study\数据库表修改.txt",'wb',encoding='utf-8') as f:
      f.write("jjjjjj")

f = open(r"C:\Users\君莫笑\Desktop\work and study\数据库表修改.txt",'wb')
try:
    f.write("fff")
except:
    pass
finally:
    f.close()