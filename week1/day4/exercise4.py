#Exercise 4: Random

import random

def ran_num(rannum):
    num = random.randint(1, 100)
    if rannum == num :
        print('Correct')
    else:
        print('Try again')

ran_num(25)