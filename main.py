# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import random

words = ["eloquent", "rectangle", "footprint", "surveillance", "alphabet", "capstone", ]
secret_word = random.choice(words)

guesses_left = 10


# getting guess
def get_guess():
    global guesses_left
    while "y" == "y":
        guess = input("Guess:")
        if not guess.islower():
            print("Your guess must be a lowercase letter")
        elif len(guess) >= 2:
            print("Guess must be exactly one character")
        elif guess not in secret_word:
            print("That letter is not in the secret word")
            guesses_left = guesses_left - 1
            break
        else:
            print("That letter is in the secret word!")
            return guess
            break


# creating list of dashes
lres = []
for i in range(len(secret_word)):
    lres.append("-")


# updating dashes with guesses
def update_dashes(word, gues):
    global lres
    for i in range(len(word)):
        if gues == word[i]:
            lres[i] = gues
    return ("").join(lres)


# going through dashes, returns True if any dashes left and False if no dashes
def check_lres():
    z = 0
    for x in lres:
        if x == "-":
            z = z + 1
    return z >= 1


# eveyrthing together
print(("").join(lres))

while guesses_left != 0 and check_lres() == True:
    print(update_dashes(secret_word, get_guess()))
    print(str(guesses_left) + " incorrect guesses left.")

# win or lose crangalutory message
if guesses_left != 0 and check_lres() == False:
    print("Congrats! You win. The word was: " + str(("").join(lres)))
if guesses_left == 0 and check_lres() == True:
    print("You lose. The word was: " + str(secret_word))

