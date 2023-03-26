# Marshall Ferguson - 3/2023
# Purpose: Generate a random combination of a note and a chord to practice

# Imports
import constants
import random

# Variables
rand_note = random.choice(constants.NOTES)
# CHORDS uses common chords, change to CHORDS_ADV for more rare/advanced chords
rand_chord = random.choice(constants.CHORDS)


def main():
    print(rand_note + ' ' + rand_chord)


main()
