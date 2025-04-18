import random

#player scores
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Enter Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        print("Invalid input")
        continue

    #lets generate random number that reprsents rock paper sciccors foe the computer
    random_number = random.randint(0, 2)
    # rock is 0, paper is 1, scissors is 2
    computer_picked = options[random_number]

    print("Computer picked", computer_picked + ".")

    # user wins
    if user_input == 'rock' and  computer_picked == 'scissors':
        print("You won!")
        user_wins += 1
        
    elif user_input == 'paper' and  computer_picked == 'rock':
        print("You won!")
        user_wins += 1
        
    elif user_input == 'scissors' and  computer_picked == 'paper':
        print("You won!")
        user_wins += 1
    
    else:
        print("You lost!")
        computer_wins += 1
    
print("You won", user_wins, "times")
print("the computer won", computer_wins, "times")
print("Goodbye!")

    