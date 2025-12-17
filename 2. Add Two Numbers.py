class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ca=0
        du=ListNode(0)
        cur=du
        while l1 or l2 or ca:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            t=val1+val2+ca
            ca=t//10
            cur.next=ListNode(t%10)
            cur=cur.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return du.next            
        
