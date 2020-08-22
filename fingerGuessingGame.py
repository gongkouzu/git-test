import random
rint('欢迎参加猜拳游戏！')
print('石头=0，剪刀=1，布=2')

n = 0
k = 0
while n < 3:
    k += 1

    print('haha')
    print('乱七八糟')
    print('当前第' + str(k) + '局游戏')
    myNumber = input('请输入猜拳对应数字：')
    myNumber = int(myNumber)
    fingerGuessingGame = ['石头', '剪刀', '布']
    print('你出了' + fingerGuessingGame[myNumber])
    computerNumbers = random.randint(0, 2)
    print('电脑出了' + fingerGuessingGame[computerNumbers])

    if (myNumber == 0 and computerNumbers == 1) or (myNumber == 1 and computerNumbers == 2) or (myNumber == 2 and computerNumbers == 0):
        print('你赢了！')
        n += 1
    elif myNumber == computerNumbers:
        print('平局！')
    else:
        print('你输了！')

    print('你已获胜' + str(n) + '局')
    print('\n')

print('游戏结束！')
