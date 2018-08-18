str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

str_array = str.split(' ')

ans_dict = {}

for index, elem in enumerate(str_array):
  if index in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
    ans_dict[elem[0]] = index
  else:
    ans_dict[elem[0:2]] = index

print(ans_dict)