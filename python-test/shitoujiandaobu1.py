import random
time = 1
win = 0
while win < 4:
    user = input("请输入对应数字，石头(1)/剪刀(2)/布(3)：")
    computer = ["1", "2", "3"]
    computerChoose = random.choice(computer)
    print("当前是第" + str(time) + "局")
    print("您出的是:", user)
    print("电脑出的是:",  computerChoose)