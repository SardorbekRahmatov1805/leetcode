'''

a='11'     # bu ikala son ham ikkilik sanoq sistemasiga 
b='1'
son=int(a,2)
son1=int(b,2)
son2=son+son1
if son2==0:
  print('0')
son3=''
while son2!=0:
  son4=son2%2
  son3=str(son4)+son3
  son2=son2//2
print(son3)
'''
# ikkinchi usul ikkilik funksiyasi bn ishlash 
a=input("Ikkilik sanoq sistemaga son kiriting")
b=input("Ikkilik sanoq sistemaga son kiriting")
son=bin(int(a,2)+int(b,2))[2:]
print(son)
