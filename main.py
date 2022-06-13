import random
def play ():
    user = input("whats your choice? 'R' for rock, 'P' for paper, 'S' for sciccors\n")
user = user.upper()

computer = random.choice(['R', 'P', 'S'])

if user == computer:
return "It's a Tie".format(computer)

is_win(user, computer);
return "You won!".format(user, computer)