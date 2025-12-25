

import string

text = input()

clean_text = ""
for ch in text:
    if ch not in string.punctuation:
        clean_text += ch

words = clean_text.split()

result = "#"
for word in words:
    result += word.capitalize()

if len(result) > 140:
    result = result[:140]

print(result)