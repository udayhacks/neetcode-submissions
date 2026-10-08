class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i ,num in enumerate(nums):
            
            cp = target - num
            if cp in seen:
                return [seen[cp], i]
            seen[num] = i
        
        