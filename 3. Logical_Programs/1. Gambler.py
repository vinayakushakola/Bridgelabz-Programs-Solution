"""
1. Gambler
    Desc -> Simulates a gambler who start with $stake and place fair $1 bets
            until he/she goes broke (i.e. has no money) or reach $goal.
            Keeps track of the number of times he/she wins and the number of bets he/she makes. Run the experiment N times, averages the results, and prints them out.
            a. I/P -> $Stake, $Goal and Number of times
            b. Logic -> Play till the gambler is broke or has won
            c. O/P -> Print Number of Wins and Percentage of Win and Loss.
"""
import random
def gambler(stake, goal):
    win = 0
    loss = 0
    total_gambles = 0
    while not ((stake == goal) or (stake == 0)):
        gambler = random.randint(0, 1)
        if gambler == 1:
            stake += 1
            print("You won \nstake =", stake, "goal = ", goal,"\n")
            win += 1
        else:
            stake -= 1
            print("You lost! \nBetter luck next time\nstake = ", stake, "goal = ", goal,"\n")
            loss += 1
        total_gambles += 1
    print("Total gambles played: ", total_gambles)
    print("Win Percentage: ", (win/total_gambles)*100)
    print("Loss Percentage: ", (loss/total_gambles)*100)
def start_game():
    choice = input("want to play? (y/n): ").lower()
    while choice == "y":
        stake = int(input("Enter the stake: "))
        while stake <= 1:
            print("Enter stake greater than 0: ")
            stake = int(input("Enter the stake: "))
        goal = int(input("Enter the goal: "))
        while goal < stake:
            print("You are playing to win\nEnter an amount greater than stake")
            goal = int(input("Enter the goal: "))
        gambler(stake, goal)
        choice = input("\nPlay again? (y/n): ")

start_game()