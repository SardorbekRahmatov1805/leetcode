son=int(input("sonni kiriting"))
while son!=1:
  yigindi=0
  for i in str(son):
    yigindi+=int(i)**2
  son=yigindi
  if son==4:
    print("FALSE")
    break
if son==1:
    print("True")	  
