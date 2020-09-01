#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on September 2020
# This program is a Number Guessing Game


import constants


def main():
    # This function checks if a guessed number is equal to 5

    # Input
    guess = int(input("Enter a number between 0 and 9: "))
    print("")

    # Process & Output
    if guess == constants.CORRECT_ANSWER:
        print("You got it right, the right number was 5!")


if __name__ == "__main__":
    main()
