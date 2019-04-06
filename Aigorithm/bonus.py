bonus1 = 100000*0.1
bonus2 = bonus1 + 100000*0.075
bonus3 = bonus2 + 200000*0.05
bonus4 = bonus3 + 200000*0.03
bonux5 = bonus4 + 400000*0.015
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
    print("bonus=", salary-money)
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
        bonus = bonux5 + (money-1000000)*0.01
        salary = money + bonus
        return salary

if __name__ == '__main__':
    getBonus()