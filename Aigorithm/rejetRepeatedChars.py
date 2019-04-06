'''
完成rejetRepeatedChars函数，从给定的字符串中剔除连续字符，只保留一个，比如aaabbbcdc，处理完之后返回abcdc。
'''
def demo(s):
    if not s:return ""
    res = []
    for i in range(len(s)):
        if i >= 1:
            if s[i] != res[-1]:
                res.append(s[i])
        else:
            res.append(s[i])
    return "".join(res)

if __name__ == "__main__":
    s = "aaabbcdc"
    print(demo(s))