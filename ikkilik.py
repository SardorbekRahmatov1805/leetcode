class Solution:
    def addBinary(self, a: str, b: str) -> str:
          
        son=int(a,2)
        son1=int(b,2)
        son3=son+son1
        if son3==0:
            return '0'
        son4=""
        while son3!=0:
            q=son3%2
            son4=str(q)+son4
            son3=son3//2
        return son4
