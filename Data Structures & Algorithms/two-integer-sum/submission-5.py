class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, val in enumerate(nums):
            comp = target - val
            if comp in hashmap:
                return [hashmap[comp], i]
            hashmap[val] = i