import re

pattern_emoji = r"([:]{2}|[*]{2})([A-Z][a-z]{2,})(\1)"

input_string = input()

cool_emojis = []
emoji_counter = 0
cool_treshold = 1

input_string_iter = re.finditer(r"\d", input_string)
for match in input_string_iter:
    current_digit = int(match.group())
    cool_treshold *= current_digit

input_string_iter = re.finditer(pattern_emoji, input_string)
for match in input_string_iter:
    emoji_counter += 1
    current_emoji = match.group()
    current_coolness = 0
    for char in current_emoji:
        if char.isalpha():
            current_coolness += ord(char)
    if current_coolness >= cool_treshold:
        cool_emojis.append(current_emoji)

print(f"Cool threshold: {cool_treshold}")
print(f"{emoji_counter} emojis found in the text. The cool ones are:")
for el in cool_emojis:
    print(el)
