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
    if (user == '石头' and computer_choice == '剪刀') or (user == '剪刀' and computer_choice== '布' ) or(user == '布' and computer_choice == '石头'):
        win += 1
        print("你赢了")
        print("您已获胜"+str(win)+"局")
    elif user == computer_choice:
        print("平局")
        print("您已获胜"+str(win)+"局")
    else:
        print("你输了")
        print("您已获胜"+str(win)+"局")
    time += 1