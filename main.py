# Import area
import random

# Variable area
items = ['rock','paper','scissors']

# Function area
def check_result(user,system):
    if user == 'rock' and system == 'rock':
        print('Tie, system answer:', system)
    elif user == 'rock' and system == 'paper':
        print('Lose, system answer:', system)
    elif user == 'rock' and system == 'scissors':
        print('Win, system answer:', system)
    elif user == 'paper' and system == 'paper':
        print('Tie, system answer:', system)
    elif user == 'paper' and system == 'rock':
        print('Win, system answer:', system)
    elif user == 'paper' and system == 'scissors':
        print('You lose, system answer:', system)
    elif user == 'scissors' and system == 'scissors':
        print('Tie, system answer:', system)
    elif user == 'scissors' and system == 'rock':
        print('You lose, system answer:', system)
    elif user == 'scissors' and system == 'paper':
        print('Win, system answer:', system)
    

# Main area
print('Welcome to rock, paper, scissors game')
while True:
    user_answer = input("\n\nPlease write your choice: ")
    system_answer = random.choice(items)
    check_result(user_answer,system_answer)
