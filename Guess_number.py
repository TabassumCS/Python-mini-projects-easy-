#working with the random module
import random

#ask the user how large of a number to generate

top_of_range = input("Type a number: ")

#test what they type is a number and greater than 0
if top_of_range.isdigit():
    top_of_range = int(top_of_range) #convert the string input to integer

    if top_of_range <= 0:
        print("Please enter a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time!")
    quit()
random_number = random.randint(0, top_of_range)

#keep asking the user to guess the number until they get it currect
guesses = 0

while True:
    guesses += 1 #increment guesses with more tries
    user_NumberGuess = input("Make a guess: ")
    if user_NumberGuess.isdigit():
        user_NumberGuess = int(user_NumberGuess)
    else:
        print("Please type a number next time!")
        continue #go back to the top of the while loop

    if user_NumberGuess == random_number:
        print("You have guessed the currect number!✅😄")
        break #stop the loop
    else:
        print("Ops, that is wrong!")

print("You guessed the number in", guesses, "guesses")

