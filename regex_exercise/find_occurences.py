import re

input_string = input().lower()

key_word = input().lower()

pattern = rf"\b({key_word})\b"

matches = re.findall(pattern, input_string)

print(len(matches))
