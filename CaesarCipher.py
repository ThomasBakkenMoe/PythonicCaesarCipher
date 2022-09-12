import argparse
import sys

# CONSTANTS
help_message = "A very helpful message"
usage = "CaesarCipher.py <SHIFT_NUMBER> <INPUT_FILE_PATH> [-d] [-h]"
special_characters_unicodes = [ord('æ'), ord('ø'), ord('å'), ord('Æ'), ord('Ø'), ord('Å')]
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

print(text)

# TODO: Dette er en workaround, det finnes en feil i håndteringen av norske bokstaver som gjør at de ikke  behandler
# TODO: shift_number == 0.
if shift_number == 0:
    output = text
    skip = True

if args.Decrypt:
    for i in range(len(text)):
        # Workaround, les over
        if skip:
            continue

        char = text[i]
        char_unicode = ord(char)

        # Exclude special characters
        if (char_unicode not in range(65, 90 + 1)) and (char_unicode not in range(97, 122 + 1)) and (
                char_unicode not in special_characters_unicodes):
            output += char
            continue

        new_char_unicode = char_unicode - shift_number
        if char.isupper():
            # Handle Norwegian characters
            if (65 > new_char_unicode > 65 - 4) or new_char_unicode > 90:
                match new_char_unicode:
                    case n if n == (65 - 1):
                        new_char_unicode = ord('Å')
                        output += chr(new_char_unicode)
                        continue
                    case n if n == (65 - 2) or n == (ord('Å') - 1):
                        new_char_unicode = ord('Ø')
                        output += chr(new_char_unicode)
                        continue
                    case n if n == (65 - 3) or n == (ord('Å') - 2) or n == (ord('Ø') - 1):
                        new_char_unicode = ord('Æ')
                        output += chr(new_char_unicode)
                        continue

                    case n if n + shift_number == ord('Å'):
                        print("CASE1")
                        print(n)
                        print(new_char_unicode)
                        new_char_unicode = (new_char_unicode - ord('Å')) + 90 + 1 + 2
                        output += chr(new_char_unicode)
                        continue
                    case n if n + shift_number == ord('Ø'):
                        print("CASE2")
                        print(n)
                        print(new_char_unicode)
                        new_char_unicode = (new_char_unicode - ord('Ø')) + 90 + 1 + 1
                        output += chr(new_char_unicode)
                        continue
                    case n if n + shift_number == ord('Æ'):
                        print("CASE3")
                        print(n)
                        print(new_char_unicode)
                        new_char_unicode = (new_char_unicode - ord('Æ')) + 90 + 1
                        output += chr(new_char_unicode)
                        continue

            # Handle Latin characters
            if new_char_unicode < 65:
                new_char_unicode = new_char_unicode - 65 + 90
            output += chr(new_char_unicode)

        # lower-case letters
        else:
            # Handle Norwegian characters
            if (97 > new_char_unicode > 97 - 4) or new_char_unicode > 122:
                match new_char_unicode:
                    case n if n == (97 - 1):
                        new_char_unicode = ord('å')
                        output += chr(new_char_unicode)
                        continue
                    case n if n == (97 - 2) or n == (ord('å') - 1):
                        new_char_unicode = ord('ø')
                        output += chr(new_char_unicode)
                        continue
                    case n if n == (97 - 3) or n == (ord('å') - 2) or n == (ord('ø') - 1):
                        new_char_unicode = ord('æ')
                        output += chr(new_char_unicode)
                        continue

                    case n if n + shift_number == ord('å'):
                        new_char_unicode = (new_char_unicode - ord('å')) + 122 + 1 + 2
                        output += chr(new_char_unicode)
                        continue
                    case n if n + shift_number == ord('ø'):
                        new_char_unicode = (new_char_unicode - ord('ø')) + 122 + 1 + 1
                        output += chr(new_char_unicode)
                        continue
                    case n if n + shift_number == ord('æ'):
                        new_char_unicode = (new_char_unicode - ord('Æ')) + 122 + 1
                        output += chr(new_char_unicode)
                        continue
            # Handle Latin characters
            if new_char_unicode < 97:
                new_char_unicode = new_char_unicode - 97 + 122

            output += chr(new_char_unicode)

# Encrypt
else:
    for i in range(len(text)):

        # Workaround, les over
        if skip:
            continue

        char = text[i]
        char_unicode = ord(char)

        # Exclude special characters
        if (char_unicode not in range(65, 90 + 1)) and (char_unicode not in range(97, 122 + 1)) and (
                char_unicode not in special_characters_unicodes):
            output += char
            continue

        new_char_unicode = char_unicode + shift_number
        if char.isupper():
            # Handle Norwegian characters
            if new_char_unicode > 90:
                print("NORWEGIAN")
                print(new_char_unicode)
                match new_char_unicode:
                    case n if n == (90 + 1):
                        print("CASE1")
                        new_char_unicode = ord('Æ')
                        output += chr(new_char_unicode)
                        continue
                    case n if n == (90 + 2) or n == (ord('Æ') + 1):
                        print("CASE2")
                        new_char_unicode = ord('Ø')
                        output += chr(new_char_unicode)
                        continue
                    case n if n == (90 + 3) or n == (ord('Æ') + 2) or n == (ord('Ø') + 1):
                        print("CASE3")
                        new_char_unicode = ord('Å')
                        output += chr(new_char_unicode)
                        continue
                    case n if n - shift_number == ord('Æ'):
                        print("CASE4")
                        new_char_unicode = (new_char_unicode - ord('Æ')) + 65 - 1 - 2
                        output += chr(new_char_unicode)
                        continue
                    case n if n - shift_number == ord('Ø'):
                        print("CASE5")
                        new_char_unicode = (new_char_unicode - ord('Ø')) + 65 - 1 - 1
                        output += chr(new_char_unicode)
                        continue
                    case n if n - shift_number == ord('Å'):
                        print("CASE6")
                        new_char_unicode = (new_char_unicode - ord('Å')) + 65 - 1
                        output += chr(new_char_unicode)
                        continue

            # Handle Latin characters
            if new_char_unicode > 90:
                new_char_unicode = new_char_unicode - 90 - 3 + 65 - 1
            output += chr(new_char_unicode)

        # lower-case letters
        else:
            # Handle Norwegian characters
            if new_char_unicode > 122:
                match new_char_unicode:
                    case n if n == (122 + 1):
                        new_char_unicode = ord('æ')
                        output += chr(new_char_unicode)
                        continue
                    case n if n == (122 + 2) or n == (ord('æ') + 1):
                        new_char_unicode = ord('ø')
                        output += chr(new_char_unicode)
                        continue
                    case n if n == (122 + 3) or n == (ord('æ') + 2) or n == (ord('ø') + 1):
                        new_char_unicode = ord('å')
                        output += chr(new_char_unicode)
                        continue
                    case n if n - shift_number == ord('æ'):
                        new_char_unicode = (new_char_unicode - ord('æ')) + 97 - 1 - 2
                        output += chr(new_char_unicode)
                        continue
                    case n if n - shift_number == ord('ø'):
                        new_char_unicode = (new_char_unicode - ord('ø')) + 97 - 1 - 1
                        output += chr(new_char_unicode)
                        continue
                    case n if n - shift_number == ord('å'):
                        new_char_unicode = (new_char_unicode - ord('å')) + 97 - 1
                        output += chr(new_char_unicode)
                        continue

            # Handle Latin characters
            if new_char_unicode > 122:
                new_char_unicode = new_char_unicode - 122 - 3 + 97 -1
            output += chr(new_char_unicode)

print(output)
