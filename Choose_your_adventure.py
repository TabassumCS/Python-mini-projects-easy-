print("Adventure Game: The Lost Treasure")
print("You find yourself standing at the entrance\n" \
"of a dark and mysterious cave, the air thick with \n" \
"the scent of earth and moss. Legend has it that a \n" \
"treasure beyond imagination lies hidden deep within \n" \
"the cave, but no adventurer has ever returned to tell the tale.\n")

name = input("What is your name: ")
print("\nWelcome ", name,". A faint glow emanates from within, casting eerie\n" \
"shadows on the walls. The path ahead splits into three directions:\n")

answer = input(" Which path do you choose: left, middle or right? ").lower()

if answer == "left":
    print("🛤️ Left Path – The Narrow Descent\n" \
    "You crawl through the tight space.\n"
    "It's dark and damp.\n"
    "Suddenly, a giant serpent blocks your way. but its sleeping\n" \
    "Do you [walk] or [run]?")
    if answer == "walk":
        print()
    elif answer == "run":
        print()
    else:
        print("Not a valid answer. Game Over")
elif answer == "middle":
    print("🛶 Middle Path: Underground Lake\n" \
    "A calm lake glows with faint blue light. A boat floats silently\n" \
    "Do you want to [swim] or [ride] the boat.")
    if answer == "swim":
        print("An angry shark attacked you. Game over💀")
    elif answer == "ride":
        print()
    else:
        print("Not a valid answer. Game Over")


elif answer == "right":
    print()
else:
    print("Not a valid answer. Game Over")