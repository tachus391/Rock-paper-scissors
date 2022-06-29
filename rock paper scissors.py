"""This program is a simple Rock, Paper, Scissors Game.
Please enter any one: Rock, Paper or Scissors"""
import random
print("Rock, paper, scissors!")
rps=["ROCK","PAPER","SCISSORS"]
print("Please input: Rock, paper, or scissors")
user=input()
user=user.upper()
print("You chose "+user)
if user not in rps:
    print("The input provided is not valid! Please enter any one: Rock, paper or scissors.")
else:
    num=random.randint(0,2)
    opt=rps[num]
    print("Computer chose "+opt)
    if opt==user:
        print("It's a TIE!")
    else:
        if (num==0 and user=="PAPER")or(num==1 and user=="SCISSORS")or(num==2 and user=="ROCK"):
            print("You win! Congratulations!")
        else:
            print("You lose! Better luck next time!")
