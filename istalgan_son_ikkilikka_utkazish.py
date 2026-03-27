def ikkilik(son):
    ikki=""
    while son!=0:
        qiymat=son%2
        ikki=str(qiymat)+ikki
        son//=2
    return ikki
sonlar=int(input("sonni kiritng"))
print(ikkilik(sonlar))
