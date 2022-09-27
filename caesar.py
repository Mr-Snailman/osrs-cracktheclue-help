# Quick script to caesar cipher the input

import string

def caesarShift(plaintext, shift):
    inputText = plaintext.upper()
    alphabet = string.ascii_uppercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return inputText.translate(table)

line1 = 'EWEDSNENEGQLHA'
line2 = 'LBGOGWHILPFNAS'

def main():
    for i in range(26):
        print('Shift: ', i)
        print(caesarShift(line1, i))
        print(caesarShift(line2, i))

main()
