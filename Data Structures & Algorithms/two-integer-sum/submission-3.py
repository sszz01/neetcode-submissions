class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        
        for i, val in enumerate(nums):
            hashmap[val] = i    
        for j, val in enumerate(nums):
            diff = target - val
            if diff in hashmap and hashmap[diff] != j:
                return [j, hashmap[diff]]
        return []
        