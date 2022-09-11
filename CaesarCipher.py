import argparse
import sys

help_message = "A very helpful message"
usage = "CaesarCipher.py <SHIFT_NUMBER> <INPUT_FILE_PATH> [-d] [-h]"
special_characters_unicodes = [ord('æ'), ord('ø'), ord('å'), ord('Æ'), ord('Ø'), ord('Å')]

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
except ValueError:
    print("Error: shift number must be numeric")
    sys.exit(1)

print(shift_number)
print(file_path)

reader = open(file_path, mode="r", encoding="utf-8")
text = reader.read()
reader.close()

output = ""

print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))

if args.Decrypt:
    print("TRUE")
else:
    print("FALSE")
    for i in range(len(text)):
        char = text[i]

        char_unicode = ord(char)
        #print(char_unicode)

        if (char_unicode not in range(65,90)) and (char_unicode not in range(97,122)) and (char_unicode not in special_characters_unicodes):
            print(char)

        # if(char.isupper()):
        #   output += chr((ord(char) + ))
        # else:
