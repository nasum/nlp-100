def cipher(input_st):
  gen_str = ''
  for index in range(len(input_st)):
    if input_st[index].isupper():
      gen_str += str(ord(input_st[index]))
    else:
      gen_str += input_st[index]
  return gen_str

input = 'Hello World'

print(cipher(input))