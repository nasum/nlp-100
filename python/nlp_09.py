import random

input_str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

str_array = input_str.split(' ')

output_str = ''

for word in str_array:
  if len(word) <= 4:
    output_str += (word)
    output_str += ' '
    continue
  first_char = word[0]
  last_char = word[len(word) - 1]
  random_str = ''
  offset_word = word[1:len(word) - 2]
  for char in random.sample(offset_word, len(offset_word)):
    random_str += char
  output_str += (first_char + random_str + last_char)
  output_str += ' '

print(output_str)