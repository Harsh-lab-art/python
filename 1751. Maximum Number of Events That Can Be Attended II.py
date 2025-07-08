class Solution(object):
    def maxValue(self, events, k):
        events.sort()
        n = len(events)
        start_days = [event[0] for event in events]
        memo = {}
        def dp(index, remaining):
            if index == n or remaining == 0:
                return 0
            if (index, remaining) in memo:
                return memo[(index, remaining)]
            next_index = bisect.bisect_right(start_days, events[index][1])
            skip = dp(index + 1, remaining)
            take = events[index][2] + dp(next_index, remaining - 1)
            memo[(index, remaining)] = max(skip, take)
            return memo[(index, remaining)]
        return dp(0, k)
