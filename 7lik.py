def yettilik(son):
  if son==0:
    return "0"
  if son<0:
    manfiy="-"
  else:
    manfiy=""
  son=abs(son)
  ruyxat=[]
  while son!=0:
    ruyxat.append(str(son%7))
    son//=7
  return manfiy+"".join(ruyxat[::-1])
chiqarish=int(input("sonni kiriting"))
print(yettilik(chiqarish))
#bu kod istalgan sonni 7 likka utkazadi 
