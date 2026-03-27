'''
son=int(input("sonni kiriting")) #sonni kiritamiz
if str(son)==str(son)[::-1]: #olingan sonni  matinga utkazib oxiridan orqaga qaytaradi
  print("palindrom son")
else:
  print("palindrom emas")
'''

def palindrom(son):
  if str(son)==str(son)[::-1]:
    return 'palindrom son'
  else:
    return "palindrom emas"
print(palindrom(121))
print(palindrom(12))
