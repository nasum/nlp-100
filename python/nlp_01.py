str = 'パタトクカシーー'
out = ''

for i in range(len(str)):
  if i % 2 == 1:
    out += str[i]

print(out)