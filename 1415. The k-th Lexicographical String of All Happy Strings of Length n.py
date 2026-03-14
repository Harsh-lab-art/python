class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 0
        res = ""
        def backtrack(curr):
            nonlocal count, res
            if len(curr) == n:
                count += 1
                if count == k:
                    res = "".join(curr)
                    return True
                return False
            for ch in ['a', 'b', 'c']:
                if curr and curr[-1] == ch:
                    continue
                curr.append(ch)
                if backtrack(curr):
                    return True
                curr.pop() 
            return False
        backtrack([])
        return res
