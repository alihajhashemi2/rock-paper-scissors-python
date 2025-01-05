# Import area
import random


# Function area
def check_result(user,system):
    if user == 'rock' and system == 'rock':
        print('Try again')
    elif user == 'rock' and system == 'paper':
        print('You lose')
    elif user == 'rock' and system == 'scissors':
        print('You win')
    elif user == 'paper' and system == 'paper':
        print('Try again')
    elif user == 'paper' and system == 'rock':
        print('You win')
    elif user == 'paper' and system == 'scissors':
        print('You lose')
    elif user == 'scissors' and system == 'scissors':
        print('Try again')
    elif user == 'scissors' and system == 'rock':
        print('You lose')
    elif user == 'scissors' and system == 'paper':
        print('You win')
    

# Main area
print('Welcome to rock, paper, scissors game')
while True:
    user_answer = input("Please write your choice: ")
