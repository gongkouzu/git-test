import random
print('欢迎参加猜拳游戏！')
print('石头=0，剪刀=1，布=2')
n = 0
k = 0

while n < 3:
    k += 1
    print('当前第' + str(k) + '局游戏')
    myNumber = input('请输入猜拳对应数字：')