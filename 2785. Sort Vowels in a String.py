class Solution(object):
    def sortVowels(self, s):
        vowels = set('aeiouAEIOU')
        vowel_list = [ch for ch in s if ch in vowels]
        vowel_list.sort()
        result = []
        vowel_index = 0
        for ch in s:
            if ch in vowels:
                result.append(vowel_list[vowel_index])
                vowel_index += 1
            else:
                result.append(ch)  
        return ''.join(result)
