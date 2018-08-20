def ngram(str, n):
  response = []
  for i in range(len(str) - 1):
    response.append(str[i:i+n])
  return response

str_1 = 'paraparaparadise'
str_2 = 'paragraph'

X = set(ngram(str_1, 2))
Y = set(ngram(str_2, 2))

print(X)
print(Y)

print('和集合')
print(X | Y)
print('積集合')
print(X & Y)
print('差集合')
print(X - Y)

print(X >= {'se'})
print(Y >= {'se'})