class Solution(object):
    def kthCharacter(self, k, operations):
        
        n = len(operations)
        lengths = [1]
        for op in operations:
            lengths.append(lengths[-1] * 2)

        shift_count = 0
        i = len(operations)

        while i > 0:
            op = operations[i - 1]
            prev_len = lengths[i - 1]

            if k <= prev_len:
                pass
            else:
                  k -= prev_len
                  if op == 1:
                    shift_count += 1
            i -= 1
        final_char = (ord('a') - ord('a') + shift_count) % 26 + ord('a')
        return chr(final_char)
        
