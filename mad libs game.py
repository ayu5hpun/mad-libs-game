# Mad libs game
# Word game where you fill in the blanks with random words

planet = input("Enter a planet: ") or "Mars"
adjective1 = input("Enter an adjective (description): ") or "stellar"
noun1 = input("Enter a noun (person, place, thing): ") or "falcon"
verb1 = input("Enter a verb (ending with 'ing'): ") or "dancing"
adjective2 = input("Enter an adjective (description): ") or "eccentric"
adjective3 = input("Enter an adjective (description): ") or "amazed"

print(f"\nLast night, I dreamed I was an astronaut on a mission to {planet}.")
print(f"My spaceship was called the {adjective1} {noun1}.")
print(f"When i landed, I met a group of {adjective2} aliens who greeted me by {verb1}.")
print(f"I was {adjective3}!")

while True:
    save = input("\nDo you want to save your story? (yes/no): ").strip().lower()

    if save == "yes":
        with open("astronaut_story.txt", "w") as file:
            file.write(f"Last night, I dreamed I was an astronaut on a mission to Mars.")
            file.write(f"My spaceship was called the {adjective1} {noun1}.")
            file.write(f"When I landed, I met a group of {adjective2} aliens who greeted me by {verb1}.")
            file.write(f"I was {adjective3}!")
        import os
        print("\nYour story has been saved to: ", os.getcwd())
        break

    elif save == "no":
        print("\nYour story was not saved.")
        break

    else:
        print("\nInvalid input. Please enter yes or no: ")

while True:
    play = input("\nWould you like to play again? Enter 'yes' to continue or anything to end the game: ").strip().lower()
    if play == "yes":
        print("\nContinuing...")
        break
    else:
        print("\nThank you for playing!")
        exit()

adjective4 = input("\nEnter an adjective (description): ") or "amazing"
adjective5 = input("Enter another adjective (description): ") or "colorful"
noun2 = input("Enter a noun (person, place, or thing): ") or "unicorn"
noun3 = input("Enter a plural noun (persons, places, or things): ") or "balloons"
verb2 = input("Enter a verb (ending with 'ing'): ") or "dancing"
adjective6 = input("Enter a adjective (description): ") or "joyful"
adjective7 = input("Enter a adjective (description): ") or "fun"

print(f"\nFor my {adjective4} birthday, we had a {adjective5} cake shaped like a {noun2}.")
print(f"Everyone wore {noun3} and played {verb2} games.")
print(f"The best part was when I got a {adjective6} gift!")
print(f"It was the most {adjective7} birthday ever!")

while True:
    save2 = input("\nDo you want to save your story? (yes/no): ").strip().lower()

    if save2 == "yes":
        with open("birthday_story.txt", "w") as file:
            file.write(f"For my {adjective4} birthday, we had a {adjective5} cake shaped like a {noun2}.")
            file.write(f"Everyone wore {noun3} and played {verb2} games.")
            file.write(f"The best part was when I got a {adjective6} gift!")
            file.write(f"It was the most {adjective7} birthday ever!")
        import os
        print("\nYour story has been saved to:", os.getcwd())
        break

    elif save2 == "no":
        print("\nYour story was not saved.")
        print("\nThank you for playing!")
        break

    else:
        print("\nInvalid input. Please enter yes or no:")