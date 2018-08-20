def ngram(str, n):
  response = []
  for i in range(len(str) - 1):
    response.append(str[i:i+n])
  return response

str = 'I am an NLPer'

print(ngram(str, 2))
print(ngram(str.split(' '), 2))