import random
time = 1
win = 0
while win < 3:
    user = input("请输入对应数字，石头(1)/剪刀(2)/布(3)：")
    computer = random.randint(1,3)
