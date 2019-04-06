import sys
def color():
    s = sys.stdin.readline().strip()
    s_list = s.replace("[","").replace("]","").replace("(","").replace(")","").replace("'","").replace("'","").split(",")
    s_dict = {}
    for n in range(0,len(s_list),2):
        if s_list[n] not in s_dict:
            s_dict[s_list[n]] = [s_list[n+1]]
        else:
            t = s_dict[s_list[n]]
            t.append(s_list[n+1])
            s_dict[s_list[n]] = t
    res = []
    for k,v in s_dict.items():
        res.append((k,v))
    return res

if __name__ == "__main__":
    print(color())