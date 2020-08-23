import random
time = 1
win = 0
while   win < 3:
    print("欢迎来到石头剪刀布小游戏")
    user = input ("请输入石头/剪刀/布:")
    punches = ['石头','剪刀','布']
    computer_choice = random.choice(punches)
    print("你输入的是：" + user)
    print("电脑输入的是："+ computer_choice)
    print("当前是第"+str(time)+"局")