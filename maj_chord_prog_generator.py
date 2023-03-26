# Marshall Ferguson - 3/2023
# Purpose: Generate a random combination of a chord progression to practice

# Imports
import constants
import random


def main():
    for _ in range(4):
        print(random.choice(constants.CHORD_PROG_MAJ))


main()
