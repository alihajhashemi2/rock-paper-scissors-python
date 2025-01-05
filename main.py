# Import area
import random

# Variable area
items = ['rock','paper','scissors']

# Function area
def check_result(user,system):
    if user == 'rock' and system == 'rock':
        print('Try again, system answer:', system)
    elif user == 'rock' and system == 'paper':
        print('You lose, system answer:', system)
    elif user == 'rock' and system == 'scissors':
        print('You win, system answer:', system)
    elif user == 'paper' and system == 'paper':
        print('Try again, system answer:', system)
    elif user == 'paper' and system == 'rock':
        print('You win, system answer:', system)
    elif user == 'paper' and system == 'scissors':
        print('You lose, system answer:', system)
    elif user == 'scissors' and system == 'scissors':
        print('Try again, system answer:', system)
    elif user == 'scissors' and system == 'rock':
        print('You lose, system answer:', system)
    elif user == 'scissors' and system == 'paper':
        print('You win, system answer:', system)
    

# Main area
print('Welcome to rock, paper, scissors game')
while True:
    user_answer = input("\n\nPlease write your choice: ")
    system_answer = random.choice(items)
    check_result(user_answer,system_answer)
