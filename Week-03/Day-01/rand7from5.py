import random


def rand5():
    return random.randint(1, 5)


def rand7():

    # Implement rand7() using rand5()
    x=rand5()*5+rand5()-5
    
    return x%7


print('Rolling 7-sided die...')
print(rand7())