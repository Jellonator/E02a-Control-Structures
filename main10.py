#!/usr/bin/env python3
# Import the sys and random modules
import sys, random
# Check that the python version is at least 3.7
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"
# Print the string "Greetings!"
print('Greetings!')
# Define an array of strings that contains the names of several colors
colors = ['red','orange','yellow','green','blue','violet','purple']
# Define a variable named play_again, and assign it to an empty string
play_again = ''
# Define a variable named best_count, and assign it to an integer named sys.maxsize, which is the maximum value for an integer.
best_count = sys.maxsize            # the biggest number

# Repeat this block of code while the variable play_again is not equal to 'n' and is not equal to 'no'.
while (play_again != 'n' and play_again != 'no'):
    # Define a variable 'match_color' and assign it to a random value from the 'colors' list
    match_color = random.choice(colors)
    # Define a variable 'count' and assign it to the integer 0.
    count = 0
    # Define a variable 'color' and assign it to an empty string
    color = ''
    # Repeat this block of color while color is not equal to 'match_color'
    while (color != match_color):
        # Ask the user what my favorite color is, and assign the result to the variable 'color'
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        # Take the lowercase of color and remove spaces from the left and right sides of it, then store the result in 'color'.
        color = color.lower().strip()
        # Increase 'count' by ``
        count += 1
        # Compare 'color' to 'match_color'
        if (color == match_color):
            # If they are equal, tell the user they are correct.
            print('Correct!')
        else:
            # Otherwise, tell them to try again, and tell them how many tries it took.
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    
    # Now that the game is finished (the user input a correct answer), tell them how many tries they took.
    print('\nYou guessed it in {} tries!'.format(count))

    # If it took the user fewer tries than it has ever taken them before (or, at least for the duration of this program)
    if (count < best_count):
        # Tell the user that this was their best guess so far
        print('This was your best guess so far!')
        # Update 'best_count' to equal 'count'
        best_count = count
    
    # Ask the user if they would like to try again
    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()

# Tell the user "Thanks for playing!"
print('Thanks for playing!')