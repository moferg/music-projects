# Marshall Ferguson - 3/2023
# Purpose: Generate a random combination of a note and a scale to practice

# Imports
import constants
import random

# Variables
rand_note = random.choice(constants.NOTES)
rand_scale = random.choice(constants.SCALES)


def main():
    print(rand_note + ' ' + rand_scale)


main()
