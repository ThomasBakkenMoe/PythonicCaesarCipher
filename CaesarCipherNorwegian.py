import argparse
from argparse import RawTextHelpFormatter
import sys

# CONSTANTS
HELP_MESSAGE = "A simple encryption algorithm that shifts the inputted letters <SHIFT_NUMBER> spaces in the alphabet.\n" \
               "Currently supports the Norwegian alphabet and ignores special character (they remain unencrypted).\n" \
               "Veni, vidi, vici"
USAGE = "CaesarCipher.py <SHIFT_NUMBER> <INPUT_FILE_PATH> [-d] [-h]"
SPECIAL_CHARACTER_UNICODES = [ord('æ'), ord('ø'), ord('å'), ord('Æ'), ord('Ø'), ord('Å')]
LETTERS_IN_ALPHABET = 29

# Control variables
# force_decrypt enables the cipher to work with negative values by using the decrypt algorithm when
# encrypting and vice versa
force_decrypt = False

alphabet = {
    ord("A"): 0,
    ord("B"): 1,
    ord("C"): 2,
    ord("D"): 3,
    ord("E"): 4,
    ord("F"): 5,
    ord("G"): 6,
    ord("H"): 7,
    ord("I"): 8,
    ord("J"): 9,
    ord("K"): 10,
    ord("L"): 11,
    ord("M"): 12,
    ord("N"): 13,
    ord("O"): 14,
    ord("P"): 15,
    ord("Q"): 16,
    ord("R"): 17,
    ord("S"): 18,
    ord("T"): 19,
    ord("U"): 20,
    ord("V"): 21,
    ord("W"): 22,
    ord("X"): 23,
    ord("Y"): 24,
    ord("Z"): 25,
    ord("Æ"): 26,
    ord("Ø"): 27,
    ord("Å"): 28
}

alphabet_reverse = {
    0: ord("A"),
    1: ord("B"),
    2: ord("C"),
    3: ord("D"),
    4: ord("E"),
    5: ord("F"),
    6: ord("G"),
    7: ord("H"),
    8: ord("I"),
    9: ord("J"),
    10: ord("K"),
    11: ord("L"),
    12: ord("M"),
    13: ord("N"),
    14: ord("O"),
    15: ord("P"),
    16: ord("Q"),
    17: ord("R"),
    18: ord("S"),
    19: ord("T"),
    20: ord("U"),
    21: ord("V"),
    22: ord("W"),
    23: ord("X"),
    24: ord("Y"),
    25: ord("Z"),
    26: ord("Æ"),
    27: ord("Ø"),
    28: ord("Å")
}

# Initialize argument parser
parser = argparse.ArgumentParser(description=HELP_MESSAGE, usage=USAGE, formatter_class=RawTextHelpFormatter)

# Define flag arguments
parser.add_argument("-d", "--Decrypt", action="store_true", help="Set the cipher to decrypt the input text")
parser.add_argument("-s", "--Save", help="Save the output to the specified file path")

# Read arguments from command line
args, unknown = parser.parse_known_args()

# Throws an error if there are too many non-flag arguments
if len(unknown) > 2:
    print("Error: too many non-flag arguments")
    sys.exit(1)

# Throws an error if a required argument is missing
try:
    shift_number = unknown[0]
    file_path = unknown[1]
except IndexError:
    print("Error: missing required arguments\nusage: " + USAGE)
    sys.exit(1)

# Converts the <SHIFT_NUMBER> argument to an int that is between 0 and 28
# Throws an error if <SHIFT_NUMBER> is not numeric
try:
    shift_number = int(shift_number)

    if shift_number < 0:
        force_decrypt = True

    # Modulo is used to make the shift number conform to "one run-through" of the alphabet
    shift_number = shift_number % LETTERS_IN_ALPHABET
except ValueError:
    print("Error: shift number must be numeric")
    sys.exit(1)

# Read the input file
text = ""
try:
    reader = open(file_path, mode="r", encoding="utf-8")
    text = reader.read()
    reader.close()
except FileNotFoundError as err:
    print(err)

output = ""

# Main encryption/decryption loop
for i in range(len(text)):
    char = text[i]
    char_unicode = ord(char.capitalize())

    # Exclude special characters
    if (char_unicode not in range(65, 90 + 1)) and (char_unicode not in SPECIAL_CHARACTER_UNICODES):
        output += char
        continue

    alphabet_index = alphabet.get(char_unicode)

    if args.Decrypt ^ force_decrypt:
        new_alphabet_index = (alphabet_index - shift_number) % LETTERS_IN_ALPHABET
    else:
        new_alphabet_index = (alphabet_index + shift_number) % LETTERS_IN_ALPHABET

    if char.isupper():
        output += chr(alphabet_reverse.get(new_alphabet_index))
    # Lower Case
    else:
        output += chr(alphabet_reverse.get(new_alphabet_index)).lower()

# Write output to file if save flag is raised
if args.Save:
    writer = open(args.Save, mode="w", encoding="utf-8")
    writer.write(output)
    writer.close()

print(output)
