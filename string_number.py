def string_number(num1,num2):
  ruyxat=[]
  dildagi=0
  i,j=len(num1)-1,len(num2)-1
  while i>=0 or j>=0 or dildagi:
    son1=int(num1[i]) if i>=0 else 0
    son2=int(num2[j]) if j>=0 else 0
    qushish=son1+son2+dildagi
    dildagi=qushish//10
    ruyxat.append(str(qushish%10))
    i-=1
    j-=1
  return "".join(ruyxat[::-1])
kirit1=input("1-sonni kiriitng")
kirit2=input("2-sonni kiriting")
print(string_number(kirit1,kirit2))
