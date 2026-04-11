def tanga(son):
  yigind=0
  while son>=0:
    yigind+=1
    son=son-yigind
  return yigind-1
son1=int(input("sonni kriiting"))
print(tanga(son1))

