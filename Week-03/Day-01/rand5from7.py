import random


def rand7():
    return random.randint(1, 7)


def rand5():

    # Implement rand5() using rand7()
    x=rand7()
    if(x>5):
        x=rand5()
    return x

print("Rolling 5-sided die...")
print(rand5())