import re

links_list = []
pattern = r'www\.[A-Za-z0-9\-]+(\.[a-z]+)+'

input_string = input()

while input_string != '':

    current_links = re.finditer(pattern, input_string)

    for link in current_links:

        links_list.append(link.group())

    input_string = input()

print(*links_list, sep='\n')
