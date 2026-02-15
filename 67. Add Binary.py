class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=[]
        i=len(a)-1
        j=len(b)-1
        carry=0
        while i>=0 or j>=0 or carry:
            d=int(a[i]) if i>=0 else 0
            e=int(b[j]) if j>=0 else 0
            s=d+e+carry
            res.append(str(s%2))
            carry=s//2
            i-=1
            j-=1
        return ''.join(res[::-1])    
        
