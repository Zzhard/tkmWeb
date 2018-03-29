import random
import math

#随机生成手机号码
def randomtelphone():
    telnum = random.choice(['139', '188', '185', '136', '158', '151', '186']) + "".join(random.sample("0123456789", 8))
    return telnum

#随机生成数字加字符串
def randomhs():
    hsnum = "123456" + "".join(random.sample('zyxwvutsrqponmlkjihgfedcba', 5))
    return hsnum


if __name__ == '__main__':
    a = randomtelphone()
    b = randomhs()

    print(a)
    print(b)