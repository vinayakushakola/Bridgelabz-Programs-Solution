"""
2. Flip Coin and print percentage of Heads and Tails
    a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.
    b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or heads
    c. O/P -> Percentage of Head vs Tails
"""

import random
def flip_coin():
    number = int(input("Enter number of times you want to flip a coin: "))
    heads = 0
    tails = 0
    if number > 0:
        for i in range(number):
            generate_random_num = random.random()
            if generate_random_num > 0.5:
                heads += 1
            else:
                tails += 1
        heads_percent = (heads/number) * 100
        tails_percent = (tails/number) * 100
        print("Percentage of heads:", heads_percent)
        print("Percentage of tails:", tails_percent)

flip_coin()