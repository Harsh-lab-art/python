class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        c=0
        i=0
        sub=[]
        for j, char in enumerate(s):
            c+=1 if char =='1' else -1
            if c==0:
                inn=self.makeLargestSpecial(s[i+1:j])
                sub.append("1"+ inn+"0")
                i=j+1
        sub.sort(reverse=True)
        return "".join(sub)        
        
