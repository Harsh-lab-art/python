class Solution(object):
    def bestClosingTime(self, customers):
        pen=customers.count('Y')
        minpen=pen
        best=0
        for i,c in enumerate(customers):
            if c=='Y':
                pen-=1
            else:
                pen+=1
            if(pen<minpen):
                minpen=pen
                best=i+1
        return best                
        
