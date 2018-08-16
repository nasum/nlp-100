import re

str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
replaced_str = re.sub(',|\.', '', str)
mapped_list = map(lambda x: len(x), replaced_str.split(' '))
print(list(mapped_list))