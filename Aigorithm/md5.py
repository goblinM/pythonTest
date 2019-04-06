encrapy = {chr(96+i):chr(64+i+1) for i in range(1,26)}
encrapy['z'] = 'A'
unencrapy = {chr(64+i):chr(96+i-1) for i in range(2,27)}
unencrapy['A'] = 'z'
print(encrapy)
print(unencrapy)
def Encrapy(s):
    res = ""
    for i in s:
        if i.isdigit():
            res += str(int(i)+1)
        else:
            res += encrapy[i]
    return res

def UnEncrapy(s):
    res = ""
    for i in s:
        if i.isdigit():
            res += str(int(i)-1)
        else:
            res += unencrapy[i]
    return res

if __name__ == "__main__":
    s1 = "BCDEF1"
    s2 = "abcde0"
    print(Encrapy(s2))
    print(UnEncrapy(s1))