class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp, counter = '', 0
        for i in s:
            temp += i
            if temp.count(i) == 2:
                counter = max(counter, len(temp)-1)
                temp = temp[temp.index(i)+1:]
        return max(counter, len(temp))