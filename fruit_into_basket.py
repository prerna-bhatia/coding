class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        if len(fruits) == 1:
            return 1
        f1 = fruits[0]
        f2 = None
        l1 = 1
        l2 = 0
        currLen = 1
        maxLen = 1
        
        for i in range(1, len(fruits)):
            if f2 == None:
                if f1 != fruits[i]:
                    l1 = 0
                    l2 = 1
                    f2 = fruits[i]
                else:
                    l1 += 1
                currLen += 1
                maxLen = max(currLen, maxLen)

            elif fruits[i] == f1:
                l1 += 1
                l2 = 0
                currLen += 1
                maxLen = max(currLen, maxLen)
            elif fruits[i] == f2:
                l2 += 1
                l1 = 0
                currLen += 1
                maxLen = max(currLen, maxLen)

            else:
                if l1 > l2:
                    f2 = fruits[i]
                    l2 = 1
                    currLen = l1 + l2
                    l1 = 0
                    maxLen = max(currLen, maxLen)
                else:
                    f1 = fruits[i]
                    l1 = 1
                    currLen = l1 + l2
                    l2 = 0
                    maxLen = max(currLen, maxLen)
        
        return maxLen