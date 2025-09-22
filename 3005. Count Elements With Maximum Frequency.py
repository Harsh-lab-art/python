class Solution(object):
    def maxFrequencyElements(self, nums):
        freq_map={}
        for num in nums:
            freq_map[num]=freq_map.get(num,0)+1
        max_freq=0
        for freq in freq_map.values():
            if freq>max_freq:
                max_freq=freq
        total_max_freq_elements = 0
        for freq in freq_map.values():
            if freq == max_freq:
                total_max_freq_elements += freq

        return total_max_freq_elements            
