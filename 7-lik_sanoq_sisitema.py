def yettilik_sanoq_sisitema(son):
  sakrash=1
  son1=0
  while son!=0:
    son2=son%7
    son//=7
    son1=son1+son2*sakrash
    sakrash*=10
  return int(son1)
son3=int(input("sonni kiriting"))
print(yettilik_sanoq_sisitema(son3))
