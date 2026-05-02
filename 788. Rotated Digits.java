class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for num in range(1, n + 1):
            s = str(num) 
            valid = True
            changed = False
            for ch in s:
                if ch in '347':
                    valid = False
                    break
                if ch in '2569':
                    changed = True
            if valid and changed:
                count += 1
        return count
