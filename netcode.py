def birxil(son):
  for i in range(len(son)):
    for j in range(i+1,len(son)):
      if son[i]==son[j]:
        return True
  return False
son2=input("sonni kiriitng")
print(birxil(son2))
