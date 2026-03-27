def roman(son):
  yigindi=0
  qiymat = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}  
  
  for i in range(len(son)-1):
    if qiymat[son[i]]>qiymat[son[i+1]]:
      yigindi+=qiymat[son[i]]
    else:
      yigindi-=qiymat[son[i]]
  yigindi+=qiymat[son[i-1]]
  return yigindi
s=input("Rim raqamini kiriting! biz sizga oddiy son kurinishida o'tkazib beramiz:")
print(roman(s)) 
