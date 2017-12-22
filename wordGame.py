import random
print('<---------------Word Game--------------->')
num = 30
guess = random.randint(0,500)
while num > 0:
    temp = input('猜猜我心里想的数字(0-500):')  # input 返回字符串类型的变量
    if guess == int(temp):
        print('wow 猜对啦')
        break
    elif guess < int(temp):
        print('bigger than I think')
        num -= 1
        print('you left {} to guess it'.format(num))
    elif guess > int(temp):
        print('smaller than I think')
        num -= 1
        print('you left {} to guess it'.format(num))
    else:
        print('stupid boys/girls')
else:
    print('游戏结束,你是真笨啊')
    print('The right answer is {}'.format(guess))