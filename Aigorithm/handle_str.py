'''
字节跳动2019的第二道编程题，按照记忆隐约来写的：
某个字母出现3次，去掉一个则是正确的单词如helllo  ->  hello
如果出现AABB形式，去掉第二个的一个字母如helloo  -> hello
如果AABBCC，按照从左到右规则，尽管AABB,BBCC都是错的，但是优先处理AABB，把AABBCC变为AABCC
比如
输入 helloo  helllo  wooooooow
输出 hello   hello   woow
'''
def handle_str(s):
    pass

if __name__ == "__main__":
    pass