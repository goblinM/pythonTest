class Solution:
    def select_ball(self,k,n,one,two,three):
        import re
        result = []

        for i in range(1,k+1):
            if one or two or three > n:
                result.append("00" + str(n))



    def two(self,one,type,string):
        t1 = "abcdefghijklmnopqrstuvwxyz0123456789"
        s_1 = dict(zip(one,t1))  # 解密
        s_2 = dict(zip(t1,one))  # 加密
        if type == 1:
            result = [s_2[i] for i in string]
        else:
            result = [s_1[i] for i in string]
        return "".join(result)

    def three(self,s1,s2):
         start = s1.index(s2[0])
         if "?" in s2:
            if s1[start]:
                pass

if __name__ == "__main__":
    obj = Solution()
    one = "fghijklmnopqrstuvwxyz0123456789abcde"
    type = 1
    string = "a3579hello"
    t = obj.two(one,type,string)
    print(t)