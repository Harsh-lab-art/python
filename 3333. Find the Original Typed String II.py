class Solution(object):
    def possibleStringCount(self, word, k):
        mod=10**9+7
        n,cnt =len(word),1
        freq=list()

        for i in range(1,n):
            if word[i]==word[i-1]:
                cnt+=1
            else:
                freq.append(cnt)
                cnt=1
        freq.append(cnt)

        ans=1
        for o in freq:
            ans=ans*o%mod
        if len(freq)>=k:
            return ans
        f,g=[1]+[0]*(k-1),[1]*k
        for i in range(len(freq)):
            fnew=[0]*k
            for j in range(1,k):
                fnew[j]=g[j-1]
                if j-freq[i]-1>=0:
                    fnew[j]=(fnew[j]-g[j-freq[i]-1])%mod
            gnew=[fnew[0]]+[0]*(k-1)
            for j in range(1,k):
                gnew[j]  =(gnew[j-1]+fnew[j])%mod
            f,g=fnew,gnew
        return (ans-g[k-1])%mod                                    
        
