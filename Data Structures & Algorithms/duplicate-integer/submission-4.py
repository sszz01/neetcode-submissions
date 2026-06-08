class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for _, val in enumerate(nums):
            if val in s:
                return True
            s.add(val)
        
        return False