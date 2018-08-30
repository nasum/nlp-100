import re

with open('./england_text.txt', mode='r') as file:
  lines = file.readlines()
  for line in lines:
    if re.search(r"Category", line):
      print(line)
  
