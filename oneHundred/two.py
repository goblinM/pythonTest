'''企业发放的奖金根据利润提成。利润(I)低于或等于 10 万元时，奖金可提 10%；利润
高
 于 10 万元，低于 20 万元时，低于 10 万元的部分按 10%提成，高于 10 万元的部分，
可可提
 成 7.5%；20 万到 40 万之间时，高于 20 万元的部分，可提成 5%；40 万到 60 万之间
时高于
 40 万元的部分，可提成 3%；60 万到 100 万之间时，高于 60 万元的部分，可提成 1.5%，
高于
 100 万元时，超过 100 万元的部分按 1%提成，从键盘输入当月利润 I，求应发放奖金
总数？'''

bonus1 = 100000*0.1
bonus2 = bonus1 + 100000*0.075
bonus3 = bonus2 + 200000*0.05
bonus4 = bonus3 + 200000*0.03
bonus5 = bonus4 + 400000*0.015
def getBonus():
    money = input("输入利润值：")
    p = Profit()
    money = int(money)
    salary = 0
    if money in range(0,100000):
        t = getattr(p,"one")
        salary = t(money)
    elif money in range(100000,200000):
        t = getattr(p, "two")
        salary = t(money)
    elif money in range(200000, 400000):
        t = getattr(p, "three")
        salary = t(money)
    elif money in range(400000, 600000):
        t = getattr(p, "four")
        salary = t(money)
    elif money in range(600000, 1000000):
        t = getattr(p, "five")
        salary = t(money)
    elif money >= 1000000:
        t = getattr(p, "six")
        salary = t(money)
    print("奖金bonus=", salary-money)
class Profit:
    def one(self,money):
        bonus = money * 0.1
        salary = money + bonus
        return salary
    def two(self,money):
        bonus = bonus1 + (money-100000)*0.075
        salary = money + bonus
        return salary
    def three(self,money):
        bonus = bonus2 + (money-200000)*0.05
        salary = money + bonus
        return salary
    def four(self,money):
        bonus = bonus3 + (money-400000)*0.03
        salary = money + bonus
        return salary
    def five(self,money):
        bonus = bonus4 + (money-600000)*0.015
        salary = money + bonus
        return salary
    def six(self,money):
        bonus = bonus5 + (money-1000000)*0.01
        salary = money + bonus
        return salary

def two():
    i = int(input('input gain:\n'))
    if i <= 100000:
        bonus = i * 0.1
    elif i <= 200000:
        bonus = bonus1 + (i - 100000) * 0.075
    elif i <= 400000:
        bonus = bonus2 + (i - 200000) * 0.05
    elif i <= 600000:
        bonus = bonus3 + (i - 400000) * 0.03
    elif i <= 1000000:
        bonus = bonus4 + (i - 600000) * 0.015
    else:
        bonus = bonus5 + (i - 1000000) * 0.01
    print('bonus = ', bonus)

if __name__ == '__main__':
    getBonus()
    two()