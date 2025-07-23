class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_substring(s, first, second, gain):
            stack = []
            score = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    score += gain
                else:
                    stack.append(ch)
            return ''.join(stack), score

        
        if x >= y:
            s, gain1 = remove_substring(s, 'a', 'b', x)
            _, gain2 = remove_substring(s, 'b', 'a', y)
        else:
            s, gain1 = remove_substring(s, 'b', 'a', y)
            _, gain2 = remove_substring(s, 'a', 'b', x)

        return gain1 + gain2
