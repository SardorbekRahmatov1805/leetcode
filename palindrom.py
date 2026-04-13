def palindrom(son):
  if son<0:
    return False
  s=0
  palindromi=son
  while son!=0:
    son1=son%10
    s=s*10+son1
    son//=10
  if s==palindromi:
    return True
  else:
   return False
son3=int(input("sonni kiriiting:"))
print(palindrom(son3))
