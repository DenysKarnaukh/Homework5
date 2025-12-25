

import string
import keyword

name = input()

valid = True

if name in keyword.kwlist:
    valid = False

elif name[0].isdigit():
    valid = False

elif name.count("_") > 1:
    valid = False


else:
    for ch in name:

        if ch.isupper():
            valid = False
            break

        if ch == " ":
            valid = False
            break

        if ch in string.punctuation and ch != "_":
            valid = False
            break

print(valid)