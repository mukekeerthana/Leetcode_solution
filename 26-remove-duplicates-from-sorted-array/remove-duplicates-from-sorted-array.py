class Solution:
    def removeDuplicates(self, values: List[int]) -> int:
        if not values:
            return 0
        
        pos = 1
        for i in range(1, len(values)):
            if values[i] != values[i - 1]:
                values[pos] = values[i]
                pos += 1
        
        return pos
