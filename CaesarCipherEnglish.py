import argparse
import sys

# CONSTANTS
help_message = "A very helpful message"
usage = "CaesarCipher.py <SHIFT_NUMBER> <INPUT_FILE_PATH> [-d] [-h]"
LETTERS_IN_ALPHABET = 29

# Initialize argument parser
parser = argparse.ArgumentParser(description=help_message, usage=usage)

# Defining arguments
parser.add_argument("-d", "--Decrypt", action="store_true", help="Set the cipher to decrypt the input text")

# Read arguments from command line
args, unknown = parser.parse_known_args()

if len(unknown) > 2:
    print("Error: too many non-flag arguments")
    sys.exit(1)

try:
    shift_number = unknown[0]
    file_path = unknown[1]
except IndexError:
    print("Error: missing required arguments\nusage: " + usage)
    sys.exit(1)

try:
    shift_number = int(shift_number)

    # Modulo is used to make the shift number conform to "one run-through" of the alphabet
    shift_number = shift_number % LETTERS_IN_ALPHABET
except ValueError:
    print("Error: shift number must be numeric")
    sys.exit(1)

reader = open(file_path, mode="r", encoding="utf-8")
text = reader.read()
reader.close()

output = ""
skip = False

if args.Decrypt:
    for i in range(len(text)):
        char = text[i]
        char_unicode = ord(char)
        new_char_unicode = char_unicode - shift_number

        # Exclude special characters
        if (char_unicode not in range(65, 90 + 1)) and (char_unicode not in range(97, 122 + 1)):
            output += char
            continue

        if (char.isupper()):
            if new_char_unicode < 65:
                new_char_unicode = new_char_unicode - 65 + 90 + 1
            output += chr(new_char_unicode)

        # Lower Case
        else:
            if new_char_unicode < 97:
                new_char_unicode = new_char_unicode - 97 + 122 + 1
            output += chr(new_char_unicode)

else:
    for i in range(len(text)):
        char = text[i]
        char_unicode = ord(char)
        new_char_unicode = char_unicode + shift_number

        # Exclude special characters
        if (char_unicode not in range(65, 90 + 1)) and (char_unicode not in range(97, 122 + 1)) and (
                char_unicode not in special_characters_unicodes):
            output += char
            continue

        if (char.isupper()):
            if new_char_unicode > 90:
                new_char_unicode = new_char_unicode - 90 + 65 - 1
            output += chr(new_char_unicode)
        # Lower Case
        else:
            if new_char_unicode > 122:
                new_char_unicode = new_char_unicode - 122 + 97 - 1
            output += chr(new_char_unicode)

print(output)
