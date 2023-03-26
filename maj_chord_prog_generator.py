# Marshall Ferguson - 3/2023
# Purpose: Generate a random four-chord chord progression to practice

# Imports
import constants
import random

# Variables
rand_maj_chord_prog = ['I']


def main():
    for _ in range(3):
        rand_maj_chord_prog.append(random.choice(constants.CHORD_PROG_MAJ))
    print(rand_maj_chord_prog)


main()
